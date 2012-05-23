<?php if (!defined(JZ_SECURE_ACCESS)) die ('Security breach detected.');
	$word_package_verify = "Vereisten";
	$word_package_verify_note = "Nu verifi�ren we of uw installatie voldoet aan de minimumvereisten en dat alle bestanden succesvol zijn uitgepakt uit het gedownloade bestand.";
	$word_checking_files = "Bezig met controle van bestanden";
	$word_checking_requirements = "Bezig met controle van vereisten";
	$word_checking = "Bezig";
	$word_files = "Bestanden:";
	$word_all_files_found = "Alle bestanden gevonden!";
	$word_files_missing = "Helaas, sommige bestanden ontbreken!";
	$word_proceed_license = "Ga door naar licentie >>";
	$word_gpl = "GNU General Public License (GPL)";
	$word_must_agree = "U moet akkoord gaan met de GPL-licentie om door te kunnen gaan.";
	$word_i_agree = "Ik ga akkoord";
	$word_you_must_agree = "U moet akkoord gaan om verder te kunnen...";
	$word_proceed_to_install = "Ga door naar installatie >> ";
	$word_install_type = "Soort installatie";
	$word_install_type_note = "Kies het soort installatie. Bij gebruik van een CMS dient u vooraf te hebben gezorgd voor een link in het CMS menusysteem, en dient de installatie van Jinzora via die link gestart te zijn ...of... als de installatie van Jinzora is voltooid, dient u eerst een link te maken in uw CMS alvorens Jinzora voor de eerste maal te starten.";
	$word_proceed_to_backend = "Ga door naar de backend configuratie >>";
	$word_backend_setup = "Backend configuratie";
	$word_backend_setup_note = "U moet aangeven hoe Jinzora gegevens leest en wegschrijft. Hiervoor bestaan verschillende opties, die in het helpvenster worden weergegeven:";
	$word_backend_type = "Soort backend:";
	$word_proceed_main_settings = "Ga door maar algemene instellingen >>";
	$word_main_settings = "Algemene instellingen";
	$word_main_settings_note = "Ok, we zijn bijna klaar. Nu moet u een aantal algemene instellingen opgeven, zodat het installatieprogramma de installatie kan voltooien en u aan de slag kunt met Jinzora 2.0";
	$word_admin_user = "Admin gebruikersnaam:";
	$word_admin_pass = "Admin wachtwoord:";
	$word_default_access = "Standaard toegangsniveau:";
	$word_no_access = "Geen toegang";
	$word_lofi = "Lo-Fi";	
	$word_user = "Standaard gebruiker";
	$word_admin = "Admin";
	$word_viewonly = "Alleen kijken";
	$word_proceed_launch = "Start Jinzora >>";
	$word_launch_jinzora = "Start Jinzora";
	$word_launch_jinzora_note = "Gefeliciteerd, u hebt de installatie succesvol doorlopen. Mocht u hulp nodig hebben, kijk dan ook even op de volgende websites.";
	$word_donations = "Jinzora Donations</strong></a><li>Do you love Jinzora, if so please consider donating to it!<br>";
	$word_website = "Jinzora Website</strong></a><li>Bezoek onze website!<br>";
	$word_forums = "Jinzora Forums</strong></a><li>Meer assistentie nodig? In de forums doen we ons uiterste best u te helpen.<br>";
	$word_docs = "Jinzora Documentation</strong></a><li>Meer informatie nodig? Raadpleeg onze online documentatie.<br>";
	$word_resources = "Jinzora informatiebronnen";
	$word_install_steps = "Installatiestappen";
	$word_language = "Taal";
	$word_license = "Licentie";
	$word_import_media = "Importeer media";
	$word_import_media_note = "Nu gaan we uw media importeren. Afhankelijk van de omvang van uw collectie kan dit enige tijd in beslag nemen. U dient enige bestanden te importeren om verder te kunnen gaan met de installatie. Op een gemiddeld systeem kunnen vijftien nummers per seconde worden verwerkt. Het maakt niet uit waar de bestanden op uw server staan.";
	$word_server_directory = "Mediadirectory:";
	$word_server_directory_note = "Geef het VOLLEDIGE pad naar uw mediabestanden op.<br><br><strong>Let op:</strong> Jinzora verwerkt gemiddeld vijftien tracks per seconde, dus met een grote collectie kan dit geruime tijd duren!";
	$word_web_path = "Web-pad:";
	$word_web_path_note = "Dit is de locatie van uw media, relatief ten opzichte van de basis-directory van uw website";
	$word_recommended = "aanbevolen";
	$word_except_testing = "behalve voor testdoeleindel";
	$word_proceed_import_media = "Ga door naar het importeren van bestanden >>";
	$word_checking_permissions = "Bezig met controle van rechten";
	$word_install_type_help = "Hier geeft u aan hoe u Jinzora wilt gebruiken. Als u Jinzora als zelfstandige applicatie wilt gebruiken, kies dan standalone Wilt u Jinzora gebruiken in een CMS-omgeving, kies dan het juiste CMS uit de lijst. De volgende CMS'en worden ondersteund: <br><br><li>Postnuke<li>PHPNuke<li>Mambo<li>CPGNuke<li>MDPro";
	$word_access_level_help = "Er zijn vier verschillende toegangsniveaus beschikbaar:<br><br><strong>Geen toegang</strong> - gebruikers MOETEN inloggen om Jinzora te gebruiken<br><br><strong>Lo-Fi</strong> - niet ingelogde gebruikers kunnen alleen lo-fi tracks afspelen<br><br><strong>Standaard gebruiker</strong> - niet ingelogde gebruikers hebben algemene toegang tot Jinzora, en hebben de mogelijkheid bestanden af te spelen<br><br><strong>Admin</strong> ALLE gebruikers hebben ALLE rechten op Jinzora<strong>GEVAARLIJKE INSTELLING!</strong";
	$word_writable = "Besschrijfbaar";
	$word_not_writable = "Niet beschrijfbaar!";
	$word_settings_perm_error = "Het lijkt erop dat het bestand settings.php niet kan worden weggeschreven. Zorg ervoor dat de webserver schrijfrechten heeft in de jinzora-directory.";
	$word_users_perm_error = "Het lijkt erop dat het bestand users.php niet kan worden weggeschreven. Zorg ervoor dat de webserver schrijfrechten heeft in de jinzora-directory.";
	$word_data_perm_error = "Het lijkt erop dat de /data directory niet beschrijfbaar is. Zorg ervoor dat de webserver schrijfrechten heeft op de data-directory in de jinzora-directory. Meestal betekent dit dat u configure.sh niet heeft uitgevoerd, of dat u de rechten niet goed heeft toegekend. Neem contact op met uw webserverbeheerder als u hierbij hulp nodig hebt.";
	$word_temp_perm_error = "Het lijkt erop dat de /temp directory niet beschrijfbaar is. Zorg ervoor dat de webserver schrijfrechten heeft op de data-directory in de jinzora-directory. Meestal betekent dit dat u configure.sh niet heeft uitgevoerd, of dat u de rechten niet goed heeft toegekend. Neem contact op met uw webserverbeheerder als u hierbij hulp nodig hebt.";
	$word_backend1_note = "Er zijn twee verschillende backend-systemen: <li><strong>Database</strong> - Gebruik een database voor de backend<li><strong>Cache</strong> - Gebruik het bestandssysteem als backend";
	$word_backend2_note = "Er zijn twee mogelijkheden voor hoe de informatie (metadata) uit uw bestanden wordt gelezen (genre, artiest, album, enzovoorts). Deze gegevens kunnen worden gelezen uit:<br><br><li><strong>het bestandssysteem</strong> - De bestandsstructuur<li><strong>ID3</strong> - de ID3 tags (of metadata) van elk bestand";
	$word_database_server = "Database server:";
	$word_database_settings = "Database instellingen:";
	$word_database_user = "Database gebruiker:";
	$word_database_pass = "Database wachtwoord:";
	$word_database_name = "Database naam:";
	$word_database_type = "Database type:";
	$word_database_continue = "Ga verder met backend-installatie";
	$word_database_connection = "Databaseverbinding";
	$word_verifying_connection = "Bezig met controle van verbinding";
	$word_creating_database = "Bezig met aanmaken database";
	$word_creating_tables = "Bezig met aanmaken tabellen";
	$word_successful = "Voltooid!";
	$word_already_exists = "Bestaat reeds";
	$word_admin_alert = "U hebt het standaard toegangsniveau ingesteld op Admin. Dit betekent dat ALLE gebruikers volledige toegang hebben tot uw gehele collectie media-bestanden!";
	$word_user_alert = "U hebt het standaard toegangsniveau zo ingesteld dat gebruikers bestanden kunnen afspelen zonder in te loggen. Zorg ervoor dat uw mediabestanden het zogenoemde streaming afspelen toestaan. Als u doorgaat vrijwaart u Jinzora van alle verantwoordelijkheden omtrent uw mediacollectie.";
	$word_cms_default_access = "Standaard toegangsniveau voor CMS-gebruikers:";
	$word_installer_help = "Jinzora help";
	$word_layout = "Media layout:";
	$word_genre_layout = "Genre";
	$word_artist_layout = "Artiest";
	$word_album_layout = "Album";
	$word_standard = "Standaard:";
	$word_custom = "Custom:";
	$word_layout_help = "Dit bepaalt de hi�rarchie voor Jinzora. U selecteert wat u als hoogste niveau voor de interface.<br><br><li><strong>Genre</strong>: Gebruik Jinzora met vier niveaus - Genre/Artiest/Album/Tracks<br><br><li><strong>Artiest</strong>: Gebruik Jinzora met drie niveaus - Artiest/Album/Tracks<br><br><li><strong>Album</strong>: Gebruik Jinzora met twee niveaus - Album/Tracks";
	$word_layout_custom_help = "Als uw collectie niet volgens een van de bovenstaande opties is gerangschikt, geef dat dan hier aan. Bijvoorbeeld:<br><i>genre/artist/track</i><br> als dat het best overeenkomt met uw structuur.<br><br>De layout is een tekenreeks die wordt gescheiden met het slash-teken '/'. U kunt gebruik maken van de volgende termen: genre, artist, album, track, generic.";
	$word_database_type = "Soort database:";
	$word_database_server_help = "Het ip-adres of de naam van uw databaseserver - meestal localhost";
	$word_database_user_help = "De gebruikersnaam waarmee u toegang krijgt tot de database";
	$word_database_password_help = "Het wachtwoord waarmee u toegang krijgt tot de database";
	$word_database_name_help = "De naam van de database die u voor Jinzora wilt gebruiken. Als deze database niet bestaat, zal Jinzora deze aanmaken.";
	$word_importing_media = "Bezig met importeren";
	$word_wait_import = "Even geduld terwijl uw bestanden worden ingelezen.";
	$word_importing = "Bezig met importeren";
	$word_import_complete = "<strong>Importeren voltooid!</strong><br>U kunt aanvullende bestanden importeren, of doorgaan met het opslaan van de configuratie.";
	$word_save_config = "Configuratie opslaan";
	$word_proceed_save_config = "Verder naar opslaan van de configuratie >>";
	$word_save_config_note = "Uw configuratie wordt opgeslagen, of ter download aangeboden als dat niet lukt";
	$word_saveing_config = "Bezig met opslaan van de configuratie";
	$word_file_create_error = "Het wegschrijven van de instellingen is niet gelukt. Zorg voor de juiste rechten, of download de onderstaande bestanden en zet ze op de juiste plaats";
	$word_download = "download";
	$word_download_and_continue = "Als u deze bestanden hebt gedownload, plaats ze dan in de root-directory van uw Jinzora-installatie. Klik vervolgens op Controleer configuratie.";
	$word_check_config = "Controleer configuratie";
	$word_found = "Gevonden!";
	$word_written_success = "Wegschrijven voltooid!";
	$word_frontend = "Interface:";
	$word_frontend_help = "Hiermee kunt u de verschillende weergaven kiezen voor Jinzora.<br><br><strong>Slick</strong> is de nieuwe standaardweergave voor Jinzora 2.0<br><br><strong>Classic</strong> is de weergave van Jinzora 1.1<br><br><strong>Media Library</strong> is een nieuwe weergave waarmee Jinzora op ��n pagina werkt<br><br><strong>Gina</strong> is gebaseerd op de Gina-applicatie";
	$word_file_found_error = "er is een configuratiebestand gevonden, maar het nieuwe bestand kan niet worden weggeschreven!";
	$word_creating_database = "Bezig met het aanmaken van de database";
	$word_creating_tables = "Bezig met het aanmaken van tabellen";
	$word_database_created = "Het aanmaken van de tabellen is zonder fouten voltooid.";
	$word_launch = "Start Jinzora 2.0";
	$word_usage_stats = "Gebruiksstatistieken";
	$word_share_stats = "Deel anonieme statistieken";
	$word_anon_stat_note = 'Wilt u anonieme statistieken delen met het Jizora ontwikkelteam? Deze gegevens worden nooit buiten het ontwikkelteam gepubliceerd, en alleen gebruikt voor het verbeteren van Jinzora. Wij verzamelen de volgende informatie:<br><br><li>Aantal tracks/genres/artiesten/albums</li><li>De omvang van uw collectie (lengte in minuten)</li><li>Gekozen backend (MySQL - Cache)</li><li>Gekozen interface (Slick, Classic, enzovoorts)</li><li>Standaard toegangsniveau (Admin, gebruiker, alleen kijken enzovoorts)</li><li>Type browser (Firefox, Mozilla, enzovoorts).<li>Versies van het OS/PHP/Webserver<li><strong>MEER NIET!</strong> (Er wordt geen enkele persoonlijke informatie verzameld!)</li><br>Bezoek onze <a target="_blank" href="http://www.jinzora.com/modules.php?op=modload&name=phpWiki&file=index&pagename=Privacy%20Policy">Jinzora Privacy Policy</a> voor meer informatie.<br><br>Deze gegevens zijn een grote hulp voor het ontwikkelteam om te begrijpen hoe we Jinzora kunnen verbetern. Deel uw anoniem statistieken!';
	$word_anan_stat_thanks = 'Dank u voor het beschikbaar stellen van anonieme gebruiksstatistieken! Wij doen ons best om uw gegevens te gebruiken om Jinzora nog beter te maken. Bezoek ook onze <a target="_blank" href="http://www.jinzora.com/modules.php?op=modload&name=phpWiki&file=index&pagename=Privacy%20Policy">Jinzora Privacy Policy</a> om precies te weten te komen hoe uw statistieken worden gebruikt';
	$word_fatal_errors = "Er zijn ernstige fouten gevonden. Verhelp deze om door te kunnen gaan met de installatie";
	$word_fatal_error = "Ernstige fout!";
	$word_minutes = "minuten";
	$word_importing_media_from = "Bezig met importeren van bestanden uit:";
	$word_import_message1 = "<strong>Bezig met het importeren van XXXXX bestanden</strong> (dit gaat ongeveer YYYY minuten duren)";
	$word_dir_invalid = "Ongeldige directory";
	$word_import_complete = "Importeren voltooid!";
	$word_complete_message = "U kunt nog meer bestanden inlezen, of Jinzora starten.<br>De volgende directory's zijn ingelezen:<br>";
	$word_database_user_help = "Geeft de gebruikersnaam waarmee u toegang krijgt tot uw database. Dit is <strong>NIET</strong> de gebruikersnaam waarmee u inlogt in Jinzora";
	$word_database_pass_help = "Geef het wachtwoord op waarmee u toegang krijgt tot uw database. Dit is <strong>NIET</strong> het wachtwoord waarmee u inlogt in Jinzora";
	$word_database_name_help = "Dit is de naam van de database die op de server wordt aangemaakt of gebruikt";
	$word_database_server_help = "Dit is de naam van de databaseserver. Als de database op dezelfde server draait als Jinzora, kunt u hier localhost invullen.";
	$word_database_type_help = "Dit is het soort database dat u gebruik voor de Jinzora installatie.";
	$word_please_select = "Maak een keuze";
	$word_share_stats = "Deel anonieme gebruiksstatistieken";
	$word_no_thanks = "Nee dank u";
	$word_your_name = "Uw naam:";
	$word_your_site = "De URL van uw website:";
	$word_comments = "Opmerkingen:";
	$word_browse_for_media = "Zoek naar media-bestanden";
	$word_directories = "Directory's";
	$word_return_to_root = "Terugkeren naar de root";
	$word_return = "Terug";
	$word_recommended_settings = "Aanbevolen instellingen";
	$word_admin_user_help = "Dit is de gebruikersnaam voor de beheerder van Jinzora. Als deze niet bestaat, wordt hij aangemaakt.";
	$word_admin_pass_help = "Dit is het wachtwoord voor de beheerdersaccount.<br><br>U dient dit wachtwoord ter controle ook in de onderstaande regel in te tikken.";
	$word_empty_import_error = "Uw media-directory is leeg. Selecteer een aantal mediabestanden om te importeren.";
	$word_php_version = "PHP versie:";
	$word_gd = "GD ondersteuning:";
	$word_iconv = "iconv ondersteuning:";
	$word_analyzing_import = "Bezig met analyseren van de te importeren bestanden";
	$word_proceed = "Doorgaan";
	$word_back = "terug";
	$word_analyze = "Analyseer";
	$word_php_version_error = 'U moet uw versie van PH opwaarderen om Jinzora 2.0 te kunnen installeren. Een nieuwere versie kunt u downloaden van www.php.net';
	$word_gd_error = '<font color="red">GD ondersteuning niet aanwezig!</font><br>Dit is geen ernstige fout, maar sommige functies voor het gebruik van plaatjes zullen niet beschikbaar zijn';
	$word_gd_error_note = "U kunt de GD libraries voor PHP downloaden van <br><br>www.boutell.com/gd/<br><br>";
	$word_iconv_error = '<font color="red">iconv ondersteuning niet aanwezig!</font><br>Dit is geen ernstige fout, maar sommige ID3-functies zullen niet beschikbaar zijn';
	$word_iconv_error_note = 'U kunt de incov libraries downloaden van <br><br>www.gnu.org/software/libiconv/<br><br>';
	$word_database = "Database";
	$word_cache = "Cache";
	$word_filesystem = "Bestandssysteem";
	$word_id3 = "ID3";
	$word_data_structure = "Datastructuur:";
	$php_session_error = "PHP Session Support is niet aanwezig. Om dit in te schakelen moet u --enable-session in uw PHP configuratie gebruiken, en controleren of de PHP sessies goed werken.";
	$word_php_session_support = "PHP Session Support:";
	$word_zend_error = "Zend Optimizer gevonden maar niet ondersteund!";
	$word_zend_error_note = "De Zend Optimizer is op uw systeem aangetroffen. Deze wordt echter (nog) niet ondersteund. Hoewel dit in de toekomst wel zal worden ondersteund, werkt Jinzora 2.0 NIET goed met de Zend Optimizer. U dient deze dan ook uit te schakelen in PHP.ini";
	$word_cms_detect = "Jinzora heeft geprobeerd uw CMS te detecteren, controleer of dit correct is, en corrigeer de instelling als dat niet zo is";
	$word_cms_db_pick = "Om de CMS-modus te kunnen gebruiken, MOET u uw huidige CMS-database ook voor Jinzora gebruiken. Dit heeft geen invloed op uw CMS. Controleer of u de juiste database gebruikt.<br><br>";
?>