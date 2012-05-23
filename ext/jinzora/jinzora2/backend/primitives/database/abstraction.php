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
 * This is the media backend for the database adaptor.
 *
 * @since 05.10.04
 * @author Ben Dodson <bdodson@seas.upenn.edu>
 */
class sqlTable {
  var $data;
  var $rows;
  
  function sqlTable() {
    $this->data = array();	
    $this->rows = 0;
  }
  
  function add($row) {
    foreach ($row as $key => $val) {
      $this->data[$this->rows][$key] = $val;
    }
    $this->rows++;
  }
}

function resultsToArray(&$results,$type = false) {
	global $backend;

  if ($type === false) {
    $arr = array();
    $hash = array();   
    for ($i = 0; $i < $results->rows; $i++) {
      if ($results->data[$i]['leaf'] == "false") {
	$me = &new jzMediaNode(jz_db_unescape($results->data[$i]['path']));
	$me->leafcount = $results->data[$i]['leafcount'];
	$me->nodecount = $results->data[$i]['nodecount'];
	$me->artpath = jz_db_unescape($results->data[$i]['main_art']);
	$me->myid = $results->data[$i]['my_id'];
	if ($me->artpath == "") {
	  $me->artpath = false;
	}
	$me->playcount = $results->data[$i]['playcount'];
	$me->dlcount = $results->data[$i]['dlcount'];
	$me->longdesc = jz_db_unescape($results->data[$i]['longdesc']);
	// Gross hack to follow;
	// Fixes case where an album is in 2 genres from 1 artist:
	if ($backend == "id3-database") {
	  if (!isset($hash[pathize(strtolower($me->getName()))])) {
	    $arr[] = $me;
	    $hash[pathize(strtolower($me->getName()))] = true;
	  }
	} else {
	  $arr[] = $me;
	}
      }
      else {
	$arr[] = &new jzMediaTrack(jz_db_unescape($results->data[$i]['path']));
      }
    }
    return $arr;
  } else if ($type == 'tracks') {
    $arr = array();
    for ($i = 0; $i < $results->rows; $i++) {
      $me = &new jzMediaTrack(jz_db_unescape($results->data[$i]['path']));
      // FILL META HERE. ***//
      if (isset($results->data[$i]['filepath']) && $results->data[$i]['filepath'] != "")
	$me->playpath = $results->data[$i]['filepath'];
      if ($results->data[$i]['trackname'] != "" && $results->data[$i]['trackname'] != "-")
	$me->title = jz_db_unescape($results->data[$i]['trackname']);
      $arr[] = $me;
    }
    return $arr;
  }
}


function jz_db_connect() {
  global $sql_type, $sql_pw, $sql_socket, $sql_db, $sql_usr;

  switch ($sql_type) {
  case "DBX_MYSQL":
    if (function_exists("mysql_query")) {
      $link = @mysql_connect($sql_socket, $sql_usr, $sql_pw);
      if (!$link) return false;
      if(!@mysql_select_db($sql_db, $link)) return false;
      
      return $link;      
    }
    break;

  case "DBX_PGSQL":
    if (function_exists("pg_query")) {
      $connect_string = "host=".$sql_socket." dbname=".$sql_db." user=".$sql_usr." password=".$sql_pw;
      $link = pg_connect($connect_string);
      return $link;
    }
    break;
    
  case "DBX_SQLITE":
    if (function_exists('sqlite_query')) {
      return sqlite_open($sql_db);
    }
    break;
    
  case "DBX_MSSQL":
    if (function_exists('mssql_query')) {
      $link = mssql_connect ($sql_socket,$sql_usr,$sql_pw);
      if (!$link) return false;
      if(!@mssql_select_db($sql_db, $link)) return false;
      
      return $link;
      
    }	
    break;
  }

  // DBX:
  switch ($sql_type) {
  case "DBX_MSSQL":
    $sqlt = DBX_MSSQL;
    break;
  case "DBX_ODBC":
    $sqlt = DBX_ODBC;
    break;
  case "DBX_FBSQL":
    $sqlt = DBX_FBSQL;
    break;
  case "DBX_SYBASECT":
    $sqlt = DBX_SYBASECT;
    break;
  case "DBX_OCI8":
    $sqlt = DBX_OCI8;
    break;
  case "DBX_SQLITE":
    $sqlt = DBX_SQLITE;
    break;
  }
  return dbx_connect($sqlt, $sql_socket, $sql_db, $sql_usr, $sql_pw);
}


function jz_db_drop() {
  global $sql_type, $sql_pw, $sql_socket, $sql_db, $sql_usr;

  switch ($sql_type) {
  case "DBX_MYSQL":
    if (function_exists("mysql_query")) {
      $link = @mysql_connect($sql_socket,$sql_usr,$sql_pw);
      if (!$link) return false;
      @mysql_query("DROP DATABASE $sql_db");
      return;
    }
    break;
  case "DBX_PGSQL":
    if (function_exists("pg_query")) {
      $connect_string = "host=".$sql_socket." user=".$sql_usr." password=".$sql_pw;
      $link = pg_connect($connect_string);
      if (!$link) return false;
      return pg_query("DROP DATABASE $sql_db");
    }
    break;
  case "DBX_MSSQL":
    if (function_exists("mssql_query")) {
      $link = @mssql_connect($sql_socket,$sql_usr,$sql_pw);
      if (!$link) return false;
      @mssql_query("DROP DATABASE $sql_db");
      return;
    }
    break;
  }

  // DBX:
  return;
}


function jz_db_create() {
  global $sql_type, $sql_pw, $sql_socket, $sql_db, $sql_usr;
  
  switch ($sql_type) {
  case "DBX_MYSQL":
    if (function_exists("mysql_query")) {
      $link = @mysql_connect($sql_socket,$sql_usr,$sql_pw);
      if (!$link) return false;
      return mysql_query("CREATE DATABASE $sql_db");
    }
    break;
  case "DBX_PGSQL":
    return false;
    /*
    $connect_string = "host=".$sql_socket." user=".$sql_usr." password=".$sql_pw;
    $link = pg_connect($connect_string);
    if (!$link) return false;
    return pg_query("CREATE DATABASE $sql_db");
    */
    break;
  case "DBX_SQLITE":
    if (function_exists('sqlite_query')) {
    	$sqliteerror = null;
      	$link = sqlite_open($sql_db, 0666, $sqliteerror);
      	if (!$link) {
      		echo $sqliteerror;
      		return false;
      	}
      	sqlite_close($link);
      	return true;
    }
    break;
  case "DBX_MSSQL":
    if (function_exists("mssql_query")) {
      $link = @mssql_connect($sql_socket,$sql_usr,$sql_pw);
      if (!$link) return false;
      return mssql_query("CREATE DATABASE $sql_db");
    }
    break;
  }

  // DBX:
  return false;
  break;
}

function jz_db_query($link, $sql) {
  global $sql_type, $sql_pw, $sql_socket, $sql_db, $sql_usr;

  switch ($sql_type) {
  case "DBX_MYSQL":
    if (function_exists("mysql_query")) {
      $results = @mysql_query($sql, $link);
      if (!$results)
	{ return false; }
      $res = &new sqlTable();
      while ($row = @mysql_fetch_array($results, MYSQL_BOTH)) {
	$res->add($row);
      }
    
      return $res;
    }
    break;

  case "DBX_PGSQL":
    if (function_exists("pg_query")) {
      $results = @pg_query($link,$sql);
      if (!$results)
	{ return false; }
      $res = &new sqlTable();
      $len = pg_num_rows($results);
      for ($i = 0; $i < $len; $i++) {
	$row = pg_fetch_array($results,$i,PGSQL_BOTH);
	$res->add($row);
      }
      return $res;
    }
    break;

  case "DBX_SQLITE":
    if (function_exists('sqlite_query')) {
      $results = @sqlite_query($link,$sql);
      if (!$results)
	{ return false; }
      $res = sqlite_fetch_all($results,SQLITE_BOTH);
      $ret = &new sqlTable();
      $ret->data = $res;
      $ret->rows = sizeof($res);
      return $ret;
    }
    break;
    
  case "DBX_MSSQL":
    if (function_exists("mssql_query")) {
      $results = @mssql_query($sql, $link);
      if (!$results)
	{ return false; }
      $res = &new sqlTable();
      while ($row = @mssql_fetch_array($results, MSSQL_BOTH)) {
	$res->add($row);
      }
      return $res;
    }
    break;
  }

  // DBX:
  return @dbx_query($link, $sql);  
}

function jz_db_error($link) {
  global $sql_type, $sql_pw, $sql_socket, $sql_db, $sql_usr;
  
  switch ($sql_type) {
  case "DBX_MYSQL":
    if (function_exists("mysql_query")) {
      return mysql_error($link);
    }
    break;
  case "DBX_PGSQL":
    if (function_exists("pg_query")) {
      return pg_last_error($link);
    }
    break;
  case "DBX_SQLITE":
    if (function_exists('sqlite_query')) {
      return sqlite_last_error($link);
    }
    break;
  case "DBX_MSSQL":
    if (function_exists("mssql_query")) {
      return mssql_get_last_message();
    }
    break;
  }

  // DBX:
    return dbx_error($link);
}

function jz_db_close($link) {
  global $sql_type;
  
  // Hack by Ross to fix things for Postnuke
  return;

  switch ($sql_type) {
  case "DBX_MYSQL":
    if (function_exists("mysql_query")) {
      return mysql_close($link);
    }
    break;
  case "DBX_PGSQL":
    if (function_exists("pg_query")) {
      return pg_close($link);
    }
    break;
  case "DBX_SQLITE":
    if (function_exists('sqlite_query')) {
      return sqlite_close($link);
    }
    break;
  case "DBX_MSSQL":
    if (function_exists('mssql_query')) {
      return mssql_close($link);
    }
    break;
  }
  

  // DBX:
    return @dbx_close($link);
}

function jz_db_escape($string) {
  global $sql_type;
  switch ($sql_type) {
  case "DBX_MYSQL":
  	return mysql_escape_string($string);
  	break;
  case "DBX_PGSQL":
  	return pg_escape_string($string);
  	break;
  case "DBX_SQLITE":
  	return sqlite_escape_string($string);
  	break;
  case "DBX_MSSQL":
    return str_replace("'","''",$string);
    break;
  default:
    return addSlashes($string);
    break;
  }
}

function jz_db_unescape($string) {
  global $sql_type;
  switch ($sql_type) {
  case "DBX_SQLITE":
    return $string;
    break;
  case "DBX_MSSQL":
  	return str_replace("''", "'", $string);
  	break;
  default:
    return stripSlashes($string);
    break;
  }
}

function jz_db_rand_function() {
  global $sql_type;
  switch ($sql_type) {
  case "DBX_MSSQL":
  	return "newid()";
  	break;
  case "DBX_PGSQL":
  case "DBX_SQLITE":
    return "random()";
    break;
  default:
    return "rand()";
  }
}

?>
