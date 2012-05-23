<?php

/* Displays the Jukebox Block
* 
* @author Ben Dodson
* @version 12/22/04
* @since 12/22/04
*/
global $this_page, $media_dirs, $jbArr, $root_dir, $include_path, $jb_art_size,
       $jzUSER, $img_delete, $img_jb_clear, $img_arrow_up, $img_arrow_down,$jukebox_display;

$smarty = smartySetup();

$display = new jzDisplay();
include_once ($include_path . "jukebox/class.php");

// let's default to stream
if (!isset ($_SESSION['jb_playwhere'])) {
	if (checkPermission($jzUSER, "stream")) {
		$_SESSION['jb_playwhere'] = "stream";
	} else {
		$_SESSION['jb_playwhere'] = $jbArr[0]['description'];
	}
}
$jb_playwhere = $_SESSION['jb_playwhere'];

$smarty->assign('jukebox_display',$jukebox_display);
$arr = array ();
$arr['action'] = "jukebox";
$arr['subaction'] = "jukebox-command";
$arr['command'] = "playwhere";

$smarty->assign('playback_dev',$jb_playwhere);
$smarty->assign('playback_dev_form_action', urlize($arr));
$smarty->assign('playback_dev_form_method','POST');
$smarty->assign('can_stream',checkPermission($jzUSER,'stream'));

// Now let's get a list of all the jukeboxes that are installed
$jbs = array();
for ($i = 0; $i < count($jbArr); $i++) {

  $def = false;
  if ($jb_playwhere == $jbArr[$i]['description']) {
    $def = true;
  }
	$jbs[] = array('id' => $jbArr[$i]['description'], 'description' => $jbArr[$i]['description'], 'default' => $def);
}
$smarty->assign('jukeboxes',$jbs);


// Now let's create our Jukebox class and connect to it to make sure it works
$jb = new jzJukebox();
if (!$jb->connect()) {
	$msg = "We had a problem connecting to the player, sorry this is a fatal error!<br><br>";
	$msg .= "Player Settings:<br>";
	for ($i = 0; $i < count($jbArr); $i++) {
		if ($jbArr[$i]['description'] == $_SESSION['jb_playwhere']) {
			foreach ($jbArr[$i] as $setting => $value) {
				$msg .= $setting . " - " . $value . "<br>";
			}
		}
	}
	$msg .= "<br>Please check these with your player's settings";
	$smarty->assign('error_message',$msg);
	return;
}


$remain = $jb->getCurrentTrackRemaining();
$jz_jbstatus = $jb->getPlayerStatus();
if ($jz_jbstatus <> "playing") {
	$remain = 0;
}
if ($remain == 1) {
	$remain = 0;
}
if ($remain > 1) {
	$remain = $remain -1;
}

if ($jb_playwhere <> "stream" && checkPermission($jzUSER, "jukebox_admin")) {
	// Ok, now we need to make sure we can do things
	$func = $jb->jbAbilities();

	if ($func['playbutton']) {
		$smarty->assign('play_button', $display->displayJukeboxButton("play", true));
	}
	if ($func['pausebutton']) {
		$smarty->assign('pause_button', $display->displayJukeboxButton("pause", true));
	}
	if ($func['stopbutton']) {
		$smarty->assign('stop_button', $display->displayJukeboxButton("stop", true));
	}
	if ($func['prevbutton']) {
		$smarty->assign('prev_button', $display->displayJukeboxButton("previous", true));
	}
	if ($func['nextbutton']) {
		$smarty->assign('next_button', $display->displayJukeboxButton("next", true));
	}
	if ($func['shufflebutton']) {
		$smarty->assign('shuffle_button', $display->displayJukeboxButton("random_play", true));
	}
	if ($func['clearbutton']) {
		$smarty->assign('clear_button', $display->displayJukeboxButton("clear", true));
	}
	
	if ($func['repeatbutton']) {
	  $status = $jb->getPlayerStatus("repeat");
	  if ($status) {
	    $smarty->assign('repeat_button', $display->displayJukeboxButton("no_repeat", true));
	  } else {
	    $smarty->assign('repeat_button', $display->displayJukeboxButton("repeat", true));
	  }
	}

	if ($func['status']) {
		$smarty->assign('jb_status', ucwords($jz_jbstatus));
	}
	if ($func['stats']) {
		$smarty->assign('jb_stats', $jb->returnJBStats());
	}
	
	$on = false;
	if ($func['progress'] and $on) {
		$smarty->assign('jb_progress',true);
	}


	if ($func['volume']) {
		$arr = array ();
		$arr['action'] = "jukebox";
		$arr['subaction'] = "jukebox-command";
		$arr['command'] = "volume";
		$smarty->assign('volume_form_action', urlize($arr));
		$smarty->assign('volume_form_method', 'POST');

		$vols = array();
		$vol = "";
		if (isset ($_SESSION['jz_jbvol-' . $_SESSION['jb_id']])) {
			$vol = $_SESSION['jz_jbvol-' . $_SESSION['jb_id']];
		}

		$c = 100;
		while ($c > 0) {
		  $def = false;
		  if ($c == $vol) {
		    $def = true;
		  }
		  $vols[] = array('value' => $c, 'label' => 'Volume ' . $c . '%', 'default' => $def);
		  $c -= 10;
		}
		$vols[] = array('value' => 0, 'label' => 'Mute', 'default' => false);
		$smarty->assign('volumes',$vols);
	}

	// This closes our if to see if we are streaming or not
}

if ($jb_playwhere <> "stream" and $func['addtype']) {

	// Now let's set the add type IF it hasn't been set
	if (!isset ($_SESSION['jb-addtype'])) {
		$_SESSION['jb-addtype'] = "current";
	}

	$arr = array ();
	$arr['action'] = "jukebox";
	$arr['subaction'] = "jukebox-command";
	$arr['command'] = "addwhere";
	$smarty->assign('addtype_form_action', urlize($arr));
	$smarty->assign('addtype_form_method', 'POST');
	$addtypes = array();

	
	
	$addtypes[] = array ('value' => 'current', 'label' => 'At Current', 'default' => ($_SESSION['jb-addtype'] == "current"));
	$addtypes[] = array ('value' => 'end', 'label' => 'At End', 'default' => ($_SESSION['jb-addtype'] == "end"));
	$addtypes[] = array ('value' => 'begin', 'label' => 'At Beginning', 'default' => ($_SESSION['jb-addtype'] == "begin"));
	$addtypes[] = array ('value' => 'replace', 'label' => 'Replace', 'default' => ($_SESSION['jb-addtype'] == "replace"));

	$smarty->assign('addtypes',$addtypes);
}

// Let's make sure they aren't streaming
if ($jb_playwhere == "stream") {
  jzTemplate($smarty, 'jukebox');
  return;
}

if ($func['nowplaying']) {
  $smarty->assign('now_playing_supported',true);
  $curTrack = $jb->getCurrentTrackName();
  $smarty->assign('now_playing_trunc', $display->returnShortName($curTrack, 25));
  $smarty->assign('now_playing_full',$curTrack);

  if ($func['nexttrack']) {
    $fullList = $jb->getCurrentPlaylist();
    if ($fullList != array ()) {
      $nextTrack = $fullList[getCurPlayingTrack() + 1];
      $fullname = $nextTrack;
      if (stristr($nextTrack, "/")) {
	$nArr = explode("/", $nextTrack);
	$nextTrack = $nArr[count($nArr) - 1];
      }
      $nextTrack = str_replace(".mp3", "", $nextTrack);
      $nextTrack = $display->returnShortName($nextTrack, 30);
    }
    $smarty->assign('next_playing_trunc', $nextTrack);
    $smarty->assign('next_playing_full', $fullname);
  }
}

if ($func['fullplaylist']) {
  if (!is_array($fullList)) {
    $fullList = $jb->getCurrentPlaylist();
  }
  // Did they need any addon tools
  $smarty->assign('addon_tools',$jb->getAddOnTools());
  // Now let's get the full playlist back
  $curTrackNum = $jb->getCurrentPlayingTrack();
  $arr = array ();
  $arr['action'] = "jukebox";
  $arr['subaction'] = "jukebox-command";
  
  $smarty->assign('playlist_form_action',urlize($arr));
  $smarty->assign('playlist_form_method','POST');

  if (isset ($_SESSION['jbSelectedItems'])) {
    $selected = $_SESSION['jbSelectedItems'];
    unset ($_SESSION['jbSelectedItems']);
  } else {
    $selected = array ();
  }
  $smarty->assign('playlist_jump_supported',$func['jump']);
  $fplaylist = array();
  for ($i = 0; $i < count($fullList); $i++) {
    $this_selected = false;
    if (false !== array_search($i, $selected)) {
      $this_selected = true;
    }
    $this_playing = false;
    if ($i == $curTrackNum) {
      $this_playing = true;
    }
    $fplaylist[] = array ('index' => $i, 'label' => $fullList[$i], 'selected' => $this_selected, 'playing' => $this_playing);
    
    
  }
  $smarty->assign('playlist', $fplaylist);

  if ($func['move']) {
    $smarty->assign('playlist_move_supported',true);

    $smarty->assign('moveup_link', 'setJbFormCommand(\'moveup\'); sendJukeboxForm(); return false;');
    $smarty->assign('moveup_button',$img_arrow_up);

    $smarty->assign('movedown_link', 'setJbFormCommand(\'movedown\'); sendJukeboxForm(); return false;');
    $smarty->assign('movedown_button',$img_arrow_down);
  }

  if ($func['delonebutton']) {
    $smarty->assign('playlist_del_supported',true);
    $smarty->assign('del_link', 'setJbFormCommand(\'delone\'); sendJukeboxForm(); return false;');
    $smarty->assign('del_button',$img_jb_clear);
  }
}

if (false) { // forget this crust for now.
  if ($jz_jbstatus == 'playing') {
    $smarty->assign('cur_track_length',$jb->getCurrentTrackLength());
    $smarty->assign('cur_track_location',$jb->getCurrentTrackLocation());
    $smarty->assign('cur_track_length_minutes',convertSecMins($curTrackLength));
  }
}

$node = false;

if (isset($jbArr[$_SESSION['jb_id']]['prefix']) && $jbArr[$_SESSION['jb_id']]['prefix'] == "http") {
  if (false !== ($id = getTrackIdFromURL($jb->getCurrentTrackPath()))) {
    $track = new jzMediaNode($id,'id');
    $node = $track->getAncestor('album');
  }
}
if (false === $node) {
  // Now we need to return the path to the track that is playing so we can get the art and description for it
  $filePath = $jb->getCurrentTrackPath();
  // Now let's create a node from that
  // First we have to get rid of the filename
  if (stristr($filePath, "\\")) {
    $pArray = explode("\\", $filePath);
  } else {
    $pArray = explode("/", $filePath);
  }
  $trackName = $pArray[count($pArray) - 1];
  // Now let's fix the track name
  $tArr = explode(".", $trackName);
  unset ($tArr[count($tArr) - 1]);
  $trackName = implode("/", $tArr);
  
  unset ($pArray[count($pArray) - 1]);
  $path = implode("/", $pArray);
  
  $mA = explode("|", $media_dirs);
  foreach ($mA as $mItem) {
    $path = str_replace(strtolower($mItem), "", strtolower($path));
  }

  // Now let's make sure we are looking at a track for real
  if ($path <> "") {
    // Now we need to remove the $media_dir from this
    $mArray = explode("|", $media_dirs);
    for ($i = 0; $i < count($mArray); $i++) {
      $path = str_replace($mArray[$i], "", $path);
    }
    $node = new jzMediaNode($path);
  }
}

if (false !== $node) {
	// Now let's set what we'll need
	$album = ucwords($node->getName());
	$parent = $node->getAncestor("artist");
	$artist = ucwords($parent->getName());

	// Now let's display the art
	if (($art = $node->getMainArt("130x130")) == false) {
		$art = "style/images/default.jpg";
	}

	if (!isset($jb_art_size)) {
	  $jb_art_size = '130';
	}
	$smarty->assign('artist',$artist);
	$smarty->assign('album',$album);
	$smarty->assign('artist_link',$display->link($parent, $artist, $artist, false, true, false, false, false, "_top"));
	$smarty->assign('album_link',$display->link($node, $album, $album, false, true, false, false, false, "_top"));
	$smarty->assign('album_url',urlize(array('jz_path' => $node->getPath("String"))));
	$smarty->assign('album_art',$display->returnImage($art, $node->getName(), $jb_art_size, $jb_art_size, "fit", false, false, "left", "5", "5"));

	// Now let's get the review
	$desc = $node->getDescription();
	$desc_truncate = 375;
	$smarty->assign('description_trunc',$display->returnShortName($desc, $desc_truncate));
	if (strlen($desc) > $desc_truncate) {
		$url_array = array ();
		$url_array['jz_path'] = $node->getPath("String");
		$url_array['action'] = "popup";
		$url_array['ptype'] = "readmore";
		$smarty->assign('description_more', '<a href="' . urlize($url_array) . '" onclick="openPopup(this, 450, 450); return false;">...read more</a>');
	}
}

jzTemplate($smarty, 'jukebox');
?>
