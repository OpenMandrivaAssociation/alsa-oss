%define beta 0
%define name alsa-oss
%define version 1.0.17

%define lib_major 0
%define pre rc4

%define lib_name %mklibname %name %lib_major
%define develname %mklibname -d %name
%if %beta
%define fname %name-%version%pre
%else
%define fname %name-%version
%endif

Summary:	Advanced Linux Sound Architecture (ALSA) library
Name:		%name
Version:	%version
%if %beta
Release:	%mkrel 0.%{pre}
%else
Release:	%mkrel 5
%endif
Epoch:		1
Source0:	ftp://ftp.alsa-project.org/pub/oss-lib/%fname.tar.bz2
Patch0:		alsa-oss-1.0.12-aoss.patch 
License:	GPL
Url:		http://www.alsa-project.org/
BuildRoot:	%_tmppath/%name-%version-root
Group:		Sound
Requires:	kernel >= 2.4.18
BuildRequires: doxygen libalsa-devel > 1.0.5

%description
Advanced Linux Sound Architecture (ALSA) is a modularized architecture which
supports quite a large range of ISA and PCI cards.
It's fully compatible with old OSS drivers (either OSS/Lite, OSS/commercial).
To use the features of alsa, one can either use:
- the old OSS api
- the new ALSA api that provides many enhanced features.

Using the ALSA api requires to use the ALSA library.
This library provides oss compatibility

%package -n %{lib_name}
Summary:    Advanced Linux Sound Architecture (ALSA) library
Group: System/Libraries
Provides:   %name
Provides:   lib%name = %version-%release

%description -n %{lib_name}
Advanced Linux Sound Architecture (ALSA) is a modularized architecture which
supports quite a large range of ISA and PCI cards.
It's fully compatible with old OSS drivers (either OSS/Lite, OSS/commercial).
To use the features of alsa, one can either use:
- the old OSS api
- the new ALSA api that provides many enhanced features.

Using the ALSA api requires to use the ALSA library.
This library provides oss compatibility

%package -n %develname
Summary:    Development files for Advanced Linux Sound Architecture (ALSA)
Group:      Development/C
Requires:   %lib_name = %epoch:%version
Obsoletes:  %{mklibname alsa-oss 1}-devel
Provides:  %{mklibname alsa-oss 1}-devel = %version-%release

%description -n %develname
Advanced Linux Sound Architecture (ALSA) is a modularized architecture which
supports quite a large range of ISA and PCI cards.
It's fully compatible with old OSS drivers (either OSS/Lite, OSS/commercial).
To use the features of alsa, one can either use:
- the old OSS api
- the new ALSA api that provides many enhanced features.

This package contains files needed in order to develop an application
that made use of ALSA.

%package -n aoss
Summary:    Wrapper script to ease ALSA-OSS compatibility library usage
Group:      Development/C
Requires:   %lib_name = %epoch:%version
Conflicts:  %{mklibname alsa-oss 1}-devel < 1.0.14-2

%description -n aoss
aoss is a simple wrapper script which facilitates the use
of the ALSA OSS compatibility library.
It just sets the appropriate LD_PRELOAD path and then runs the command.

This is useful in cases where routing settings (which can
be made in your .asoundrc file) need to be applied to commands that use the
OSS API.


%prep
%setup -q -n %fname
%patch0 -p1

%build
autoreconf -fiv
%configure2_5x
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="%ldflags -ldl"

%install
mkdir -p %{buildroot}%_includedir/sys
mkdir -p %{buildroot}%_libdir
%makeinstall_std
rm -f %{buildroot}%_libdir/libaoss.a

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %lib_name -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %lib_name -p /sbin/ldconfig
%endif

%files -n %lib_name
%defattr(-, root, root)
%doc COPYING
%_libdir/*.so.%{lib_major}*

%files -n %develname
%defattr(-,root,root)
%doc COPYING
%_libdir/*.a
%_libdir/*.la
%_libdir/*.so
%_includedir/oss-redir.h

%files -n aoss
%defattr(-,root,root)
%doc COPYING
%_bindir/aoss
%_mandir/man1/aoss.*
