{if $error_message}
<table width="100%" cellpadding="0" cellspacing="0" border="0" class="jz_block_td" height="100%">
	<tr>
		<td width="5%" valign="top" height="100%">
			<nobr>
			{$error_message}
			<br>
			Playback to:<br>
			<form action="{$playback_dev_form_action}" method="{$playback_dev_form_method}">
				<select name="jbplaywhere" class="jz_select" id="jukeboxSelect" style="width:142;" onChange="updateJukebox(true); return false;">
					{if $can_stream}
						<option 
							{if $playback_dev == "stream"}
								selected
							{/if}
							value="stream">Stream
						</option>
					{/if}
					{foreach from=$jukeboxes item=jb key=id}
						<option value="{$jb.id}" {if $jb.default}selected{/if}>{$jb.description}</option>
					{/foreach}
				</select>
			</form>
			</nobr>
		</td>
	</tr>
</table>

{else}
<table width="100%" cellpadding="3" cellspacing="0" border="0" height="100%">
	<tr>
		<td width="5%" valign="top" height="100%">
			<nobr>
			{if $playback_dev != "stream"}
				{$play_button}
				{$pause_button}
				{$stop_button}
				{$prev_button}
				{$next_button}
				{$shuffle_button}
				{$clear_button}
				<!--
				{$repeat_button}
				 -->
				<br/><br/>
				{if $jb_status}
					Status: {$jb_status}
					<br/>
				{/if}
				{if $jb_progress}
				Progress:
				<span id="timer">&nbsp;<br></span><br>
				{/if}
				<script>
				<!--			
				NextTicker_start();
				CurTicker_start();
				//-->
				</script>
				<script>setTimeout('jukeboxUpdater()',10*1000);</script>
				{/if}
			{/if}
		{if $volume_form_action}
		<form action="{$volume_form_action}" method="{$volume_form_method}">
			<input type="hidden" name="action" value="jukebox">
			<input type="hidden" name="subaction" value="jukebox-command">
			<input type="hidden" name="command" value="volume">
			<select name="jbvol" id="jukeboxVolumeSelect" class="jz_select" style="width:142;" onChange="sendJukeboxVol(); return false">
			{foreach from=$volumes item=vol key=id}
				<option value="{$vol.value}" {if $vol.default}selected{/if}>
				  {$vol.label}
				</option>
			{/foreach}
			</select>
		</form>
		<br/>
		{/if}
		Playback to:<br>
		<form action="{$playback_dev_form_action}" method="{$playback_dev_form_method}">
		<select name="jbplaywhere" class="jz_select" id="jukeboxSelect" style="width:142;" onChange="updateJukebox(true); return false;">
			{if $can_stream}
				<option {if $playback_dev == "stream"}selected{/if} value="stream">Stream</option>
			{/if}
			{foreach from=$jukeboxes item=jb key=id}
				<option value="{$jb.id}" {if $jb.default}selected{/if}>{$jb.description}</option>
			{/foreach}
		</select>
		</form>
		<br/>
		{if $addtype_form_action}
		Add type:<br />
		<form action={$addtype_form_action} method={$addtype_form_method}>
			<input type="hidden" name="action" value="jukebox">
			<input type="hidden" name="subaction" value="jukebox-command">
			<input type="hidden" name="command" value="addwhere">
			<select name="addplat" class="jz_select" id="jukeboxAddTypeSelect" style="width:142;" onChange="sendJukeboxAddType(); return false;">
			{foreach from=$addtypes item=addtype key=id}
				<option value="{$addtype.value}" {if $addtype.default}selected{/if}>
					{$addtype.label}
				</option>
			{/foreach}
			</select>
		</form>
		{/if}
		{if $playlist_move_supported or $playlist_del_supported}
			<div id="jbPlaylistButtons">
				Playlist Control:
				{if $playlist_move_supported}
				<a href="#" onclick="{$moveup_link}">{$moveup_button}</a>
				<a href="#" onclick="{$movedown_link}">{$movedown_button}</a>
				{/if}
				{if $playlist_del_supported}
				<a href="#" onclick="{$del_link}">{$del_button}</a>
				{/if}
			</div>
			{/if}
		</nobr>
		</td>
		<td width="5%" valign="top">
		{if $now_playing_supported}
			Now Playing: <span title="{$now_playing_full}">{$now_playing_trunc}</span><br/>
			<!--
			  <span ID="CurTicker" STYLE="overflow:hidden; width:275px;"  onmouseover="CurTicker_PAUSED=true" onmouseout="CurTicker_PAUSED=false">
			  </span>
			  -->
			Next Track: <span title="{$next_playing_full}">{$next_playing_trunc}</span><br/>
			<!--
			<span ID="NextTicker" STYLE="overflow:hidden; width:275px;"  onmouseover="NextTicker_PAUSED=true" onmouseout="NextTicker_PAUSED=false">
			</span>
			-->
			<br/>
		{/if}
		{if $playlist_form_action}
		Complete Playlist {$addon_tools}<br/>
		<form action="{$playlist_form_action}" method="{$playlist_form_method}" id="jbPlaylistForm">
			<input type="hidden" name="action" value="jukebox">
			<input type="hidden" name="subaction" value="jukebox-command">
			<input type="hidden" id="jbCommand" name="command" value="jumpto">
			<select multiple name="jbjumpto[]" id="jukeboxJumpToSelect" class="jz_select" size="7" style="width:275px;" {if $playlist_jump_supported}ondblclick="setJbFormCommand('jumpto'); sendJukeboxForm(); return false;"{/if}>

				{foreach from=$playlist item=track key=id}
					<option value="{$track.index}" 
						{if $track.selected}selected{/if} 
						{if $track.playing}style="font-weight:bold;">* 
						{else}>
						{/if}
						{$track.label}
					</option>
				{/foreach}
			</select>
		</form>
		{/if}
		</td>
		<td width="90%" valign="top">

{literal}<!--
		<script> 
		var seconds = '{/literal}{$cur_track_location}{literal}';
		var time = '';
		t = document.getElementById("timer");	
		
		function converTime(sec){
			ctr=0;
			while (sec >= 60){
				sec = sec - 60;
				ctr++;
			}
			if (ctr<0){ctr=0}
			if (sec<0){sec=0}
			if (sec < 10){sec = "0" + sec;}							
			return ctr + ":" + sec;
		}
		
		function displayCountdown(){ 
		  return;
		// Update the counter
			seconds++	
				
			// Now let's not go over
			if (seconds < {/literal}{$cur_track_length}{literal}){
				t.innerHTML = converTime(seconds) + "/{/literal}{$cur_track_length_minutes}{literal}";
			} else {
				t.innerHTML = "{/literal}{$cur_track_length_minutes}/{$cur_track_length_minutes}{literal}";
				seconds = 1;
				updateJukebox(true);
			}
			setTimeout("displayCountdown()",1000);
		} 
		displayCountdown(); 
		</script> 
-->{/literal}
		{if $artist_link}
			{$artist_link} - {$album_link}
			<br/>{$album_art}
			{$description_trunc}
			{if $description_more}
			{$description_more}
			{/if}
		{/if}
		</td>
	</tr>
</table>