%define lib_major 0

%define libname %mklibname %{name} %{lib_major}
%define devname %mklibname -d %{name}

Summary:	Advanced Linux Sound Architecture (ALSA) library
Name:		alsa-oss
Version:	1.1.6
Release:	1
Epoch:		1
License:	GPL
Group:		Sound
Url:		http://www.alsa-project.org/
Source0:	ftp://ftp.alsa-project.org/pub/oss-lib/%{name}-%{version}.tar.bz2
Patch0:		alsa-oss-1.0.12-aoss.patch
BuildRequires:	doxygen
BuildRequires:	pkgconfig(alsa)

%description
Advanced Linux Sound Architecture (ALSA) is a modularized architecture which
supports quite a large range of ISA and PCI cards.
It's fully compatible with old OSS drivers (either OSS/Lite, OSS/commercial).
To use the features of alsa, one can either use:
- the old OSS api
- the new ALSA api that provides many enhanced features.

Using the ALSA api requires to use the ALSA library.
This library provides oss compatibility

%package -n %{libname}
Summary:	Advanced Linux Sound Architecture (ALSA) library
Group:		System/Libraries
Provides:	%{name} = %{EVRD}

%description -n %{libname}
Advanced Linux Sound Architecture (ALSA) is a modularized architecture which
supports quite a large range of ISA and PCI cards.
It's fully compatible with old OSS drivers (either OSS/Lite, OSS/commercial).
To use the features of alsa, one can either use:
- the old OSS api
- the new ALSA api that provides many enhanced features.

Using the ALSA api requires to use the ALSA library.
This library provides oss compatibility

%package -n %{devname}
Summary:	Development files for Advanced Linux Sound Architecture (ALSA)
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel  = %{EVRD}

%description -n %{devname}
Advanced Linux Sound Architecture (ALSA) is a modularized architecture which
supports quite a large range of ISA and PCI cards.
It's fully compatible with old OSS drivers (either OSS/Lite, OSS/commercial).
To use the features of alsa, one can either use:
- the old OSS api
- the new ALSA api that provides many enhanced features.

This package contains files needed in order to develop an application
that made use of ALSA.

%package -n aoss
Summary:	Wrapper script to ease ALSA-OSS compatibility library usage
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n aoss
aoss is a simple wrapper script which facilitates the use
of the ALSA OSS compatibility library.
It just sets the appropriate LD_PRELOAD path and then runs the command.

This is useful in cases where routing settings (which can
be made in your .asoundrc file) need to be applied to commands that use the
OSS API.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fiv
%configure
%make CFLAGS="%{optflags} -O0" LDFLAGS="%{ldflags} -ldl"

%install
mkdir -p %{buildroot}%{_includedir}/sys
mkdir -p %{buildroot}%{_libdir}

%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.a

%files -n %{libname}
%{_libdir}/*.so.%{lib_major}*

%files -n %{devname}
%doc COPYING
%{_libdir}/*.so
%{_includedir}/oss-redir.h

%files -n aoss
%{_bindir}/aoss
%{_mandir}/man1/aoss.*
