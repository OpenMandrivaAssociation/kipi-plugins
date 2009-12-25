Name: kipi-plugins
Version: 1.0.0
Release: %mkrel 1
Summary: KDE image Interface Plugins
License: GPLv2+
Group: System/Libraries
Source0: http://downloads.sourceforge.net/kipi/%{name}-%{version}.tar.bz2
URL: http://www.kipi-plugins.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Epoch: 1
Requires: mjpegtools 
Requires: vorbis-tools 
Requires: mpg123
Requires: imagemagick >= 5.5.4
BuildRequires: kde4-macros
BuildRequires: kdelibs4-devel
BuildRequires: libkipi-devel
BuildRequires: libgpod-devel
BuildRequires: kdegraphics4-devel
BuildRequires: tiff-devel 
BuildRequires: libMagick-devel 
BuildRequires: libxslt-devel
BuildRequires: libgphoto-devel 
BuildRequires: imlib2-devel 
BuildRequires: libxml2-utils
BuildRequires: libmesaglu-devel
BuildRequires: opencv-devel
BuildRequires: kdepimlibs4-devel
Obsoletes:     %{_lib}kipi-plugins0 < 1:0.2.0-0.824094.3

%description
 The library of the KDE Image Plugin Interface.  

 Libkipi allows image applications to use a plugin architecture 
 for additional functionality  such as: RawConverter, SlideShow, 
 ImagesGallery, HTMLExport, PrintAssistant...

%files -f %name.lang
%defattr(-,root,root)
%doc README
%{_kde_bindir}/dngconverter
%{_kde_bindir}/scangui
%dir %{_kde_datadir}/doc/%{name}/htmlexport
%{_kde_datadir}/doc/%{name}/htmlexport/THEME_HOWTO
%dir %{_kde_datadir}/doc/%{name}/printimages
%{_kde_datadir}/doc/%{name}/printimages/TEMPLATE_HOWTO
%{_kde_datadir}/applications/kde4/scangui.desktop
%{_kde_datadir}/applications/kde4/dngconverter.desktop
%{_kde_datadir}/applications/kde4/kipiplugins.desktop
%{_kde_datadir}/apps/*
%{_kde_libdir}/kde4/kipiplugin_*
%{_kde_iconsdir}/*/*/*/*
%{_kde_datadir}/kde4/services/kipiplugin_*

#----------------------------------------------------------------------------

%define kipiplugins_major 1
%define lib_name %mklibname kipiplugins %kipiplugins_major

%package -n %lib_name
Summary:	Library files for %{name}
Group:		System/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts: %{_lib}kipi-plugins0

%description -n %lib_name
Library files for %{name}

%files -n %lib_name
%defattr(-,root,root)
%{_kde_libdir}/libkipiplugins.so.%{kipiplugins_major}*

#----------------------------------------------------------------------------

%package devel
Summary: Development files for %{name}
Group: Development/C
Requires: %{lib_name} = %{epoch}:%{version}-%{release}
Obsoletes: %{_lib}kipi-plugins-devel < 1:0.2.0

%description devel
Development files for %{name}

%files devel
%defattr(-,root,root)
%{_kde_libdir}/*.so

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version} 

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

install -d %{buildroot}/%{_kde_datadir}/doc/%{name}/htmlexport/
install -d %{buildroot}/%{_kde_datadir}/doc/%{name}/printimages/
install -m644 %{buildroot}/%{_kde_datadir}/apps/kipiplugin_htmlexport/THEME_HOWTO -D %{buildroot}/%{_kde_datadir}/doc/%{name}/htmlexport/THEME_HOWTO
install -m644 %{buildroot}/%{_kde_datadir}/apps/kipiplugin_printimages/TEMPLATE_HOWTO -D %{buildroot}/%{_kde_datadir}/doc/%{name}/printimages/TEMPLATE_HOWTO

#removing wrong files
rm -f %{buildroot}/%{_kde_datadir}/apps/kipiplugin_htmlexport/THEME_HOWTO
rm -f %{buildroot}/%{_kde_datadir}/apps/kipiplugin_printimages/TEMPLATE_HOWTO

%find_lang %name --all-name

%clean
rm -rf %buildroot


