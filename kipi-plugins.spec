# Disable until libmediawiki gets individual tarball release
%bcond_with wikimedia
%bcond_with vkontakte

Name:		kipi-plugins
Summary:	KDE Image Plugin Interface plugins
Url:		https://projects.kde.org/projects/extragear/graphics/kipi-plugins
Epoch:		2
Version:	5.9.1
Release:	2
License:	GPLv2+
Group:		Graphics
Source0:	http://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
#Patch0:		digikam-5.9.0-exiv2-0.27.patch
Suggests:	kipi-plugins-dlna
Suggests:	kipi-plugins-dropbox
Suggests:	kipi-plugins-jalbum
Suggests:	kipi-plugins-facebook
Suggests:	kipi-plugins-flashexport
Suggests:	kipi-plugins-flickr
Suggests:	kipi-plugins-googleservices
Suggests:	kipi-plugins-imageshack
Suggests:	kipi-plugins-imgurexport
Suggests:	kipi-plugins-kmlexport
Suggests:	kipi-plugins-piwigoexport
Suggests:	kipi-plugins-printimages
Suggests:	kipi-plugins-rajceexport
Suggests:	kipi-plugins-remotestorage
Suggests:	kipi-plugins-sendimages
Suggests:	kipi-plugins-smug
%if %{with vkontakte}
Suggests:	kipi-plugins-vkontakte
%else
Obsoletes:	kipi-plugins-vkontakte < %{EVRD}
%endif
%if %{with wikimedia}
Suggests:	kipi-plugins-wikimedia
%else
Obsoletes:	kipi-plugins-wikimedia < %{EVRD}
%endif
Suggests:	kipi-plugins-yandexfotki
Obsoletes:	kipi-plugins-panorama < 5.0.0-0.beta4.2
Obsoletes:	kipi-plugins-expoblending < 5.0.0-0.beta4.2
BuildRequires:	doxygen
BuildRequires:	eigen3
BuildRequires:	flex
BuildRequires:	lld
BuildRequires:	bison
BuildRequires:	imagemagick
BuildRequires:	mariadb-server
BuildRequires:	mariadb-devel
BuildRequires:	tiff-devel
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(ImageMagick)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(jasper)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(lensfun)
BuildRequires:	pkgconfig(libusb)
BuildRequires:	pkgconfig(libgphoto2)
BuildRequires:	pkgconfig(libgpod-1.0)
BuildRequires:	pkgconfig(libpgf)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(lqr-1) >= 0.4.0
BuildRequires:	pkgconfig(opencv)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(expat)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(QtAV)
BuildRequires:	cmake(QtAVWidgets)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5WebKitWidgets)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	cmake(Qt5MultimediaWidgets)
BuildRequires:	cmake(Qt5XmlPatterns)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5AkonadiContact)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5FileMetaData)
BuildRequires:	cmake(KF5Kipi)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KF5ThreadWeaver)
BuildRequires:	cmake(KF5Sane)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(Marble)
BuildRequires:	cmake make
# (tpg) needed if build with GCC
BuildRequires:	gomp-devel

%rename kipi-plugins-advancedslideshow
%rename kipi-plugins-picasa
%rename kipi-plugins-photivo
%rename kipi-plugins-gpssync
%rename kipi-plugins-acquireimages
%rename kipi-plugins-batchprocess
%rename kipi-plugins-calendar
%rename kipi-plugins-debianscreenshot
%rename kipi-plugins-dlna
%rename kipi-plugins-dngconverter
%rename kipi-plugins-galleryexport
%rename kipi-plugins-htmlexport
%rename kipi-plugins-imageviewer
%rename kipi-plugins-ipodexport
%rename kipi-plugins-jpeglossless
%rename kipi-plugins-kioexportimport
%rename kipi-plugins-metadataedit
%rename kipiplugin-photolayouts-editor
%rename kipi-plugins-rawconverter
%rename kipi-plugins-removeredeyes
%rename kipi-plugins-shwup
%rename kipi-plugins-timeadjust
%rename kipi-plugins-videoslideshow

%description
The library of the KDE Image Plugin Interface.

Libkipi allows image applications to use a plugin architecture
for additional functionality such as: RawConverter, SlideShow, 
ImagesGallery, HTMLExport, PrintAssistant...

%files -f kipi-plugins.lang
%doc AUTHORS COPYING README TODO NEWS
%{_kde5_applicationsdir}/kipiplugins.desktop

#-----------------------------------------------------------------------

%define libkipiplugins_major %{version}
%define libkipiplugins %mklibname KF5kipiplugins %{libkipiplugins_major}

%package -n %{libkipiplugins}
Summary:	Runtime library for %{name}
Group:		System/Libraries
Obsoletes:	%{_lib}kipiplugins2 < 2:3.0.0
Obsoletes:	%{_lib}kipiplugins3 < 2:4.0.0

%description -n %{libkipiplugins}
Library File needed by %{name}

%files -n %{libkipiplugins}
%{_kde5_libdir}/libKF5kipiplugins.so.%{libkipiplugins_major}*

#-----------------------------------------------------------------------

%package dropbox
Summary:	Dropbox export Kipi Plugin
Group:		System/Libraries
Requires:	kipi-common

%description dropbox
A tool to export images to a remote Dropbox web service.

%files dropbox -f kipiplugin_dropbox.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_dropboxui.rc
%{_qt5_plugindir}/kipiplugin_dropbox.so
%{_kde5_services}/kipiplugin_dropbox.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-dropbox.*

#-----------------------------------------------------------------------

%package jalbum
Summary:	jAlbum export Kipi Plugin
Group:		System/Libraries
Requires:	kipi-common

%description jalbum
A tool to export images to a remote jAlbum.

%files jalbum -f kipiplugin_jalbum.lang
%{_qt5_plugindir}/kipiplugin_jalbum.so
%{_iconsdir}/hicolor/*/apps/kipi-jalbum.png
%{_kde5_services}/kipiplugin_jalbum.desktop
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_jalbumui.rc

#-----------------------------------------------------------------------

%package facebook
Summary:	Facebook Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description facebook
A tool to import/export images to/from a remote Facebook web service.

%files facebook -f kipiplugin_facebook.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_facebookui.rc
%{_qt5_plugindir}/kipiplugin_facebook.so
%{_kde5_services}/kipiplugin_facebook.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-facebook.*

#-----------------------------------------------------------------------

%package flashexport
Summary:	Flash export Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description flashexport
A tool to export images to Flash.

%files flashexport -f kipiplugin_flashexport.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_flashexportui.rc
%{_kde5_datadir}/kipiplugin_flashexport
%{_qt5_plugindir}/kipiplugin_flashexport.so
%{_kde5_services}/kipiplugin_flashexport.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-flash.*

#-----------------------------------------------------------------------

%package flickr
Summary:	Flick Export Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description flickr
A tool to export images to a remote Flickr, 23 and Zoomr web services.

%files flickr -f kipiplugin_flickr.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_flickrui.rc
%{_qt5_plugindir}/kipiplugin_flickr.so
%{_kde5_services}/kipiplugin_flickr.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-flickr.*
%{_kde5_iconsdir}/hicolor/*/apps/kipi-hq.*

#-----------------------------------------------------------------------

%package googleservices
Summary:	Google services export Kipi Plugin
Group:		System/Libraries
Requires:	kipi-common
%rename kipi-plugins-googledrive
%rename kipi-plugins-picasa

%description googleservices
A tool to export images to a remote services.

%files googleservices -f kipiplugin_googleservices.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_googleservicesui.rc
%{_qt5_plugindir}/kipiplugin_googleservices.so
%{_kde5_services}/kipiplugin_googleservices.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-googledrive.*
%{_kde5_iconsdir}/hicolor/*/apps/kipi-googlephoto.*

#-----------------------------------------------------------------------

%package remotestorage
Summary:    Export pictures to or import from a remote directory that is accessible via KIO
Group:      System/Libraries
Requires:   kipi-common

%description remotestorage
A tool to export pictures to or import from a remote
directory that is accessible via KIO

%files remotestorage -f kipiplugin_remotestorage.lang
%{_qt5_plugindir}/kipiplugin_remotestorage.so
%{_kde5_datadir}/kservices5/kipiplugin_remotestorage.desktop
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_remotestorageui.rc

#-----------------------------------------------------------------------


%package imageshack
Summary:	Imageshack Export Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	kipi-common

%description imageshack
A tool to export images to ImageShack.

%files imageshack -f kipiplugin_imageshack.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_imageshackui.rc
%{_qt5_plugindir}/kipiplugin_imageshack.so
%{_kde5_services}/kipiplugin_imageshack.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-imageshack.*

#-----------------------------------------------------------------------

%package imgurexport
Summary:	Imgur Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	kipi-common

%description imgurexport
A tool to export pictures to Imgur.

%files imgurexport -f kipiplugin_imgur.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_imgurui.rc
%{_qt5_plugindir}/kipiplugin_imgur.so
%{_kde5_services}/kipiplugin_imgur.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-imgur.*

#-----------------------------------------------------------------------

%package kmlexport
Summary:	Create KML files to present images with coordinates
Group:		System/Libraries
Requires:	kipi-common

%description kmlexport
A plugin to create KML files to present images with coordinates.

%files kmlexport -f kipiplugin_kmlexport.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_kmlexportui.rc
%{_qt5_plugindir}/kipiplugin_kmlexport.so
%{_kde5_services}/kipiplugin_kmlexport.desktop

#-----------------------------------------------------------------------

%package piwigoexport
Summary:	Piwi Go Export
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description piwigoexport
A tool to export images to a remote Piwigo.

%files piwigoexport -f kipiplugin_piwigo.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_piwigoui.rc
%{_qt5_plugindir}/kipiplugin_piwigo.so
%{_kde5_datadir}/kipiplugin_piwigo
%{_kde5_services}/kipiplugin_piwigo.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-piwigo.*

#-----------------------------------------------------------------------

%package printimages
Summary:	Print Images Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description printimages
A tool to print images in various formats.

%files printimages -f kipiplugin_printimages.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_printimagesui.rc
%{_qt5_plugindir}/kipiplugin_printimages.so
%{_kde5_services}/kipiplugin_printimages.desktop
%{_kde5_datadir}/kipiplugin_printimages/

#-----------------------------------------------------------------------

%package rajceexport
Summary:	Rajce.net Exporter
Group:		System/Libraries
Requires:	libkdcraw-common
Requires:	kipi-common

%description rajceexport
A tool to export images to a remote rajce.net service.

%files rajceexport -f kipiplugin_rajce.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_rajceui.rc
%{_qt5_plugindir}/kipiplugin_rajce.so
%{_kde5_services}/kipiplugin_rajce.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-rajce.*

#-----------------------------------------------------------------------

%package sendimages
Summary:	Send Images kipi plugins
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description sendimages
A tool to send images by e-mail.

%files sendimages -f kipiplugin_sendimages.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_sendimagesui.rc
%{_qt5_plugindir}/kipiplugin_sendimages.so 
%{_kde5_services}/kipiplugin_sendimages.desktop

#-----------------------------------------------------------------------

%package smug
Summary:	Smug Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description smug
A tool to import/export images to/from SmugMug web service.

%files smug -f kipiplugin_smug.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_smugui.rc
%{_qt5_plugindir}/kipiplugin_smug.so
%{_kde5_services}/kipiplugin_smug.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-smugmug.*

#-----------------------------------------------------------------------
%if %{with vkontakte}
%package vkontakte
Summary:	VKontakte.ru Exporter
Group:		System/Libraries
Requires:	kipi-common

%description vkontakte
A tool to export on VKontakte.ru Web service

%files vkontakte -f kipiplugin_vkontakte.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_vkontakteui.rc
%{_qt5_plugindir}/kipiplugin_vkontakte.so
%{_kde5_services}/kipiplugin_vkontakte.desktop
%endif

#-----------------------------------------------------------------------

%if %{with wikimedia}
%package wikimedia
Summary:	Wikimedia Export Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	kipi-common

%description wikimedia
A tool to export images to a remote MediaWiki site

%files wikimedia -f kipiplugin_mediawiki.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_wikimediaui.rc
%{_qt5_plugindir}/kipiplugin_wikimedia.so
%{_kde5_services}/kipiplugin_wikimedia.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-wikimedia.*
%endif

#-----------------------------------------------------------------------

%package yandexfotki
Summary:	Yandex.Fotki Exporter
Group:		System/Libraries
Requires:	libkdcraw-common
Requires:	kipi-common

%description yandexfotki
A tool to export images to a remote Yandex.Fotki web service.

%files yandexfotki -f kipiplugin_yandexfotki.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_yandexfotkiui.rc
%{_qt5_plugindir}/kipiplugin_yandexfotki.so
%{_kde5_services}/kipiplugin_yandexfotki.desktop

#-----------------------------------------------------------------------

%prep
%autosetup -p1

%build
# (tpg) upstream ships own libraw library instead of using system-wide libraw
# make[2]: Leaving directory '/builddir/build/BUILD/digikam-5.5.0/build'
# /usr/bin/ld: warning: ../libs/rawengine/libraw/liblibraw.a(demosaic_packs.cpp.o): multiple common of '.gomp_critical_user_.var'
# /usr/bin/ld: ../libs/rawengine/libraw/liblibraw.a(libraw_cxx.cpp.o): previous definition here
# /builddir/build/BUILD/digikam-5.5.0/core/libs/rawengine/libraw/src/libraw_xtrans_compressed.cpp:130: error: undefined reference to '__kmpc_global_thread_num'
# try to build with GCC because of above issue
#export CC=gcc
#export CXX=g++

%cmake_kde5 -G "Unix Makefiles" \
	-DENABLE_OPENCV3:BOOL=ON \
	-DENABLE_MYSQLSUPPORT:BOOL=ON \
	-DENABLE_INTERNALMYSQL:BOOL=OFF \
	-DENABLE_AKONADICONTACTSUPPORT:BOOL=ON \
	-DENABLE_APPSTYLES:BOOL=ON \
	-DENABLE_KFILEMETADATASUPPORT:BOOL=ON \
	-DENABLE_MEDIAPLAYER:BOOL=ON

%make_build

%install
%make_install -C build

# PO files for stuff that isn't part of kipi-plugins
rm -f %{buildroot}%{_kde5_datadir}/locale/*/LC_MESSAGES/digikam.mo
rm -f %{buildroot}%{_kde5_datadir}/locale/*/LC_MESSAGES/libkipi.mo

# devel "library" without headers is useless
rm -f %{buildroot}%{_libdir}/libKF5kipiplugins.so

# Plugin not ready for production yet, disabled upstream

rm -f %{buildroot}%{_kde5_datadir}/locale/*/LC_MESSAGES/kipiplugin_photivointegration.mo
%if %{without wikimedia}
rm -f %{buildroot}%{_kde5_datadir}/locale/*/LC_MESSAGES/kipiplugin_mediawiki.mo
%endif
%if %{without vkontakte}
rm -f %{buildroot}%{_kde5_datadir}/locale/*/LC_MESSAGES/kipiplugin_vkontakte.mo
rm -f %{buildroot}%{_kde5_datadir}/locale/*/LC_MESSAGES/libkvkontakte.mo
%endif

%find_lang kipi-plugins kipiplugins kipi-plugins.lang --with-html || touch kipi-plugins.lang

%find_lang kipiplugin_acquireimages || touch kipiplugin_acquireimages.lang
%find_lang kipiplugin_advancedslideshow || touch kipiplugin_advancedslideshow.lang
%find_lang kipiplugin_batchprocessimages || touch kipiplugin_batchprocessimages.lang
%find_lang kipiplugin_debianscreenshots || touch kipiplugin_debianscreenshots.lang
%find_lang kipiplugin_dlnaexport || touch kipiplugin_dlnaexport.lang
%find_lang kipiplugin_dngconverter || touch kipiplugin_dngconverter.lang
%find_lang kipiplugin_dropbox || touch kipiplugin_dropbox.lang
%find_lang kipiplugin_facebook || touch kipiplugin_facebook.lang
%find_lang kipiplugin_flashexport || touch kipiplugin_flashexport.lang
%find_lang kipiplugin_flickr || touch kipiplugin_flickr.lang
%find_lang kipiplugin_galleryexport || touch kipiplugin_galleryexport.lang
%find_lang kipiplugin_googleservices || touch kipiplugin_googleservices.lang
%find_lang kipiplugin_gpssync || touch kipiplugin_gpssync.lang
%find_lang kipiplugin_htmlexport || touch kipiplugin_htmlexport.lang
%find_lang kipiplugin_imageshack || touch kipiplugin_imageshack.lang
%find_lang kipiplugin_imageviewer || touch kipiplugin_imageviewer.lang
%find_lang kipiplugin_imgur || touch kipiplugin_imgur.lang
%find_lang kipiplugin_ipodexport || touch kipiplugin_ipodexport.lang
%find_lang kipiplugin_jalbumexport || touch kipiplugin_jalbumexport.lang
%find_lang kipiplugin_jpeglossless || touch kipiplugin_jpeglossless.lang
%find_lang kipiplugin_kioexportimport || touch kipiplugin_kioexportimport.lang
%find_lang kipiplugin_kmlexport || touch kipiplugin_kmlexport.lang
%find_lang kipiplugin_kopete || touch kipiplugin_kopete.lang
%find_lang kipiplugin_metadataedit || touch kipiplugin_metadataedit.lang
%find_lang kipiplugin_photolayouteditor || touch kipiplugin_photolayouteditor.lang
%find_lang kipiplugin_piwigo || touch kipiplugin_piwigo.lang
%find_lang kipiplugin_printimages || touch kipiplugin_printimages.lang
%find_lang kipiplugin_rajce || touch kipiplugin_rajce.lang
%find_lang kipiplugin_rawconverter || touch kipiplugin_rawconverter.lang
%find_lang kipiplugin_removeredeyes || touch kipiplugin_removeredeyes.lang
%find_lang kipiplugin_remotestorage || touch kipiplugin_remotestorage.lang
%find_lang kipiplugin_sendimages || touch kipiplugin_sendimages.lang
%find_lang kipiplugin_shwup || touch kipiplugin_shwup.lang
%find_lang kipiplugin_smug || touch kipiplugin_smug.lang
%find_lang kipiplugin_timeadjust || touch kipiplugin_timeadjust.lang
%find_lang kipiplugin_videoslideshow || touch kipiplugin_videoslideshow.lang
%find_lang kipiplugin_vkontakte || touch kipiplugin_vkontakte.lang
%find_lang kipiplugin_yandexfotki || touch kipiplugin_yandexfotki.lang
%find_lang kipiplugin_mediawiki || touch kipiplugin_mediawiki.lang
%find_lang kipiplugin_jalbum || kipiplugin_jalbum.lang
%find_lang libkgeomap || touch libkgeomap.lang
%find_lang libkvkontakte || touch libkvkontakte.lang
