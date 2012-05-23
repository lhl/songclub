<?php if (!defined(JZ_SECURE_ACCESS)) die ('Security breach detected.');
	/**
	* - JINZORA | Web-based Media Streamer -  
	* 
	* Jinzora is a Web-based media streamer, primarily desgined to stream MP3s 
	* (but can be used for any media file that can stream from HTTP). 
	* Jinzora can be integrated into a CMS site, run as a standalone application, 
	* or integrated into any PHP website.  It is released under the GNU GPL.
	* 
	* - Resources -
	* - Jinzora Author: Ross Carlson <ross@jasbone.com>
	* - Web: http://www.jinzora.org
	* - Documentation: http://www.jinzora.org/docs	
	* - Support: http://www.jinzora.org/forum
	* - Downloads: http://www.jinzora.org/downloads
	* - License: GNU GPL <http://www.gnu.org/copyleft/gpl.html>
	* 
	* - Contributors -
	* Please see http://www.jinzora.org/modules.php?op=modload&name=jz_whois&file=index
	* 
	* - Code Purpose -
	* This is the media backend for the default XML cache adaptor.
	*
	* @since 05.10.04
	* @author Ross Carlson <ross@jinzora.org>
	*/
	
	class jzMediaNode extends jzRawMediaNode {
		function jzMediaNode($arg = array(),$mode="path") {
			$this->_constructor($arg,$mode);
		}
		
		
		/**
		 * Adds files to the cache based on ID3.
		 * 
		 * @author Ben Dodson
		 * @version 10/15/04
		 * @since 10/15/04
		 */
		function updateCache($recursive = true, $media_path = false, $showstatus = false, $force = false, $readID3 = true) {
		  global $media_dirs;
			if ($recursive === false) {
				return false; // can't do it.
			}
			if ($media_path === false) {
			  return false;
			}
			else {
				// it doesn't matter what root it was called from;
				// the full cache must be rebuilt.
				$root = &new jzMediaNode();
				$be = &new jzBackend();
				
				$rl_name = 'reverse_lookup-' . str_replace(':','',str_replace('\\','-',str_replace('/','-',$media_path)));
				$LOOKUP = $be->loadData($rl_name);
				if (!is_array($LOOKUP)) $LOOKUP = array();
				$LOOKUP_RET = array();
				$root->updateCacheHelper("",$media_path,$be,$showstatus,$force,$readID3,$LOOKUP,$LOOKUP_RET);
				foreach ($LOOKUP as $filepath => $jz_path) {
				  // Delete these jz_paths; they are deleted files.
				  // UNLESS They were just renamed.
				  if (false === array_search($jz_path,$LOOKUP_RET)) {
				    $rt = new jzMediaTrack($jz_path);
				    $this->removeMedia($rt);
				  }
				}
				$be->storeData($rl_name,$LOOKUP_RET);
			}
		}
		
		function updateCacheHelper($path,$media_path,&$be, $showstatus,$force = false,$readID3 = true,&$LOOKUP,&$LOOKUP_RET) {
			global $audio_types, $video_types, $hierarchy,$default_art,$ext_graphic;
			
			$bestImage = "";
			$albums = array();

			if ($path != "")
				$dir = $media_path . "/" . $path;
			else
				$dir = $media_path;
			
			if (!is_readable($dir)) return false;
			if ($showstatus === true){
			  showStatus($media_path);
			} else if ($showstatus == "cli") {
			  echo word("Scanning: ") . $dir . "\n";
			}
			
			$updated = $be->getUpdated($dir);
			
			if (is_string($hierarchy))
				$hierarchy = explode("/",$hierarchy);
			
			if ($this->getLevel() > 0)
				die("Error: updateCacheHelper called from non-root.");
				
			if (!($handle = opendir($dir))) 
				die("Could not access directory $dir");
			
			while ($file = readdir($handle)) {
				if ($path == "")
					$fpath = $file;
				else
					$fpath = $path . "/" . $file;
				
				$mfpath = $media_path . "/" . $fpath;
				
				if ($file == "." || $file == "..") {
					continue;
				}
				else if (is_dir($mfpath)) {
					$this->updateCacheHelper($fpath,$media_path,$be,$showstatus,$force,$readID3,$LOOKUP,$LOOKUP_RET);
				}
				else if (preg_match("/\.($ext_graphic)$/i", $file) && !stristr($file,".thumb.")) {
				  // An image
				  if (@preg_match("/($default_art)/i",$file)) {
				    $bestImage = $mfpath;
				  } else if ($bestImage == "") {
				    $bestImage = $mfpath;
				  }
				}
				  else if (preg_match("/\.($audio_types)$/i", $file) || preg_match("/\.($video_types)$/i", $file)) {
					if ((date("U",filemtime($mfpath)) > $updated) || $force) {
						// Set path so when getFileName is called and the filepath was not found,
						// we get the correct path.
						$track = &new jzMediaTrack($mfpath);
						$track->playpath = $mfpath;
						$meta = $track->getMeta("file",$installer);
						
						// Now let's show status if we should
						if($showstatus){
							if (($_SESSION['jz_import_full_progress'] % 50 == 0) 
								or ($_SESSION['jz_import_full_progress'] == 0)
								or ($_SESSION['jz_import_full_progress'] == 1)){
								showStatus();
							}
						}

						$arr = array();
						if (isset($meta['genre'])) {
							$arr['genre'] = $meta['genre'];
						}
						if (isset($meta['subgenre'])) {
							$arr['subgenre'] = $meta['subgenre'];
						}
						if (isset($meta['artist'])) {
							$arr['artist'] = $meta['artist'];
						}
						if (isset($meta['album'])) {
							$arr['album'] = $meta['album'];
						}
						if (isset($meta['disk'])) {
							$arr['disk'] = $meta['disk'];
						}
						if (isset($meta['filename'])) {
							$arr['track'] = $meta['filename'];
						}
						
						
						$pathstring = implode("/",buildPath($arr));
						  
						  $_SESSION['jz_import_full_progress']++;

						  $add_me = true;
						  if (isset($LOOKUP[$mfpath])) {
						    if ($LOOKUP[$mfpath] == $pathstring) {
						      $add_me = false;
						    } else {
						      // Delete old instance.
						      $rt = new jzMediaTrack($LOOKUP[$mfpath]);
						      $this->removeMedia($rt);
						    }
						  }
						  
						  if ($add_me) {
						    if (($child = $this->inject($arr,$mfpath,$meta)) !== false) {
						      $album = $child->getAncestor("album");
						      if ($album !== false) {
								$albums[$album->getPath("String")] = true;
						      }
						    }
						  }
						  unset($LOOKUP[$mfpath]);
						  $LOOKUP_RET[$mfpath] = $pathstring;
					} else {
					  // Unmodified file; Keep it in the new lookup file,
					  // and take it out of the old so it doesn't get removed.
					  $LOOKUP_RET[$mfpath] = $LOOKUP[$mfpath];
					  unset($LOOKUP[$mfpath]);
					}
				  }
			}
			//$be->setUpdated($dir);
			if ($bestImage != "") {
			  foreach ($albums as $ap => $true) {
			    $album = new jzMediaNode($ap);
			    $album->addMainArt($bestImage);
			  }
			}
		}
        }

	class jzMediaTrack extends jzRawMediaTrack {
		function jzMediaTrack($arg = array(),$mode="path") {
			$this->_constructor($arg,$mode);
		}
	}
?>
