%define rev 824094

Name: kipi-plugins
Version: 0.2.0
Release: %mkrel 0.%rev.1
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
BuildRequires: libkexiv2-devel
BuildRequires: libkdcraw-devel
BuildRequires: tiff-devel 
BuildRequires: libMagick-devel 
BuildRequires: libxslt-devel
BuildRequires: libgphoto-devel 
BuildRequires: imlib2-devel 
BuildRequires: libxml2-utils
BuildRequires: libmesaglu-devel

%description
 The library of the KDE Image Plugin Interface.  

 Libkipi allows image applications to use a plugin architecture 
 for additional functionality  such as: RawConverter, SlideShow, 
 MpegEncoder, ImagesGallery, PrintWizard, CdArchiving...

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README TODO
%_kde_bindir/images2mpg
%{_kde_datadir}/doc/HTML/*
%{_kde_datadir}/apps/*
%{_kde_datadir}/config.kcfg/*
%{_kde_datadir}/services/kde4/*

#----------------------------------------------------------------------------

%define major 2
%define lib_name %mklibname kipi %major

%package -n %lib_name
Summary:	Library files for %{name}
Group:		System/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n %lib_name
Library files for %{name}

%post -n %lib_name -p /sbin/ldconfig
%postun -n %lib_name -p /sbin/ldconfig

%files -n %lib_name
%defattr(-,root,root)
%{_kde_libdir}/kde3/kipiplugin_*
%{_kde_libdir}/libkipiplugins.so.*

#----------------------------------------------------------------------------

%define lib_dev %mklibname kipi -d

%package -n %lib_dev
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{lib_name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-devel = %{epoch}:%{version}-%{release}

%description -n %lib_dev
Development files for %{name}

%files -n %lib_dev
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


