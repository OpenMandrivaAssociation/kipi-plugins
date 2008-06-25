%define rev 824094

Name: kipi-plugins
Version: 0.2.0
Release: %mkrel 0.%rev.2
Summary: KDE image Interface Plugins
License: GPLv2+
Group: System/Libraries
Source0: %{name}-%{version}.%rev.tar.bz2
URL: http://www.kipi-plugins.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Epoch: 1
Requires: mjpegtools 
Requires: vorbis-tools 
Requires: mpg123
Requires: ImageMagick >= 5.5.4
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
Conflicts: %{_lib}kipi-plugins0

%description
 The library of the KDE Image Plugin Interface.  

 Libkipi allows image applications to use a plugin architecture 
 for additional functionality  such as: RawConverter, SlideShow, 
 MpegEncoder, ImagesGallery, PrintWizard, CdArchiving...

%files
%defattr(-,root,root)
%doc README
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

%post -n %lib_name -p /sbin/ldconfig
%postun -n %lib_name -p /sbin/ldconfig

%files -n %lib_name
%defattr(-,root,root)
%{_kde_libdir}/libkipiplugins.so.%{kipiplugins_major}*

#----------------------------------------------------------------------------

%package devel
Summary: Development files for %{name}
Group: Development/C
Requires: %{lib_name} = %{epoch}:%{version}-%{release}

%description devel
Development files for %{name}

%files devel
%defattr(-,root,root)
%{_kde_libdir}/*.so

#----------------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf %buildroot


