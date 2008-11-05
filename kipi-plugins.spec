%define rev beta3

Name: kipi-plugins
Version: 0.2.0
Release: %mkrel 1.%rev.1
Summary: KDE image Interface Plugins
License: GPLv2+
Group: System/Libraries
Source0: %{name}-%{version}-%rev.tar.bz2
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
Obsoletes:     %{_lib}kipi-plugins0 < 1:0.2.0-0.824094.3

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
%lang(be) %_datadir/locale/be/*
%lang(ar) %_datadir/locale/ar/*
%lang(ca) %_datadir/locale/ca/*
%lang(da) %_datadir/locale/da/*
%lang(de) %_datadir/locale/de/*
%lang(cs) %_datadir/locale/cs/*
%lang(el) %_datadir/locale/el/*
%lang(es) %_datadir/locale/es/*
%lang(et) %_datadir/locale/et/*
%lang(ga) %_datadir/locale/ga/*
%lang(fr) %_datadir/locale/fr/*
%lang(gl) %_datadir/locale/gl/*
%lang(hi) %_datadir/locale/hi/*
%lang(ja) %_datadir/locale/ja/*
%lang(it) %_datadir/locale//it/*
%lang(km) %_datadir/locale/km/*
%lang(lv) %_datadir/locale/lv/*
%lang(nb) %_datadir/locale/nb/*
%lang(ms) %_datadir/locale/ms/*
%lang(nl) %_datadir/locale/nl/*
%lang(nn) %_datadir/locale/nn/*
%lang(oc) %_datadir/locale/oc/*
%lang(pa) %_datadir/locale/pa/*
%lang(pl) %_datadir/locale/pl/*
%lang(pt) %_datadir/locale/pt/*
%lang(ro) %_datadir/locale/ro/*
%lang(se) %_datadir/locale/se/*
%lang(ru) %_datadir/locale/ru/*
%lang(sk) %_datadir/locale/sk/*
%lang(th) %_datadir/locale/th/*
%lang(sv) %_datadir/locale/sv/*
%lang(tr) %_datadir/locale/tr/*
%_datadir/locale/uk/*
%lang(nds) %_datadir/locale/nds/*
%lang(pt_BR) %_datadir/locale/pt_BR/*
%lang(zh_CN) %_datadir/locale/zh_CN/*


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
Conflicts: %{_lib}kipi-plugins-devel < 1:0.2.0

%description devel
Development files for %{name}

%files devel
%defattr(-,root,root)
%{_kde_libdir}/*.so

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}-%{rev} 

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf %buildroot


