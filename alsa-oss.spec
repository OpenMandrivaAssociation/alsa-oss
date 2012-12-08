%define lib_major 0

%define libname %mklibname %{name} %{lib_major}
%define devname %mklibname -d %{name}

Summary:	Advanced Linux Sound Architecture (ALSA) library
Name:		alsa-oss
Version:	1.0.25
Release:	2
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
%configure2_5x
%make CFLAGS="%{optflags} -O0" LDFLAGS="%{ldflags} -ldl"

%install
mkdir -p %{buildroot}%{_includedir}/sys
mkdir -p %{buildroot}%{_libdir}

%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.a

%files -n %{libname}
%doc COPYING
%{_libdir}/*.so.%{lib_major}*

%files -n %{devname}
%doc COPYING
%{_libdir}/*.so
%{_includedir}/oss-redir.h

%files -n aoss
%doc COPYING
%{_bindir}/aoss
%{_mandir}/man1/aoss.*


%changelog
* Tue Jan 31 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1:1.0.25-1
+ Revision: 769954
- Update to 1.0.25
- Get rid of some legacy constructs in spec file

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.17-7
+ Revision: 662762
- mass rebuild

* Sun Oct 24 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1:1.0.17-6mdv2011.0
+ Revision: 588698
- make the devel package have generic provides

* Sat Nov 14 2009 Frederik Himpe <fhimpe@mandriva.org> 1:1.0.17-5mdv2010.1
+ Revision: 466079
- Replace solink patch with patch from Fedora which deals correctly
  with x86_64 lib64 directory (fixes bug #55126)

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.17-4mdv2010.0
+ Revision: 413025
- rebuild

* Fri Mar 06 2009 Emmanuel Andry <eandry@mandriva.org> 1:1.0.17-3mdv2009.1
+ Revision: 350133
- use autoreconf
- protect major

* Wed Jul 16 2008 Colin Guthrie <cguthrie@mandriva.org> 1:1.0.17-2mdv2009.0
+ Revision: 236498
- New version: 1.0.17
- Remove invalid UTF8 from spec

* Tue Jun 10 2008 Thierry Vignaud <tv@mandriva.org> 1:1.0.15-2mdv2009.0
+ Revision: 217477
- fix underlinking
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Oct 16 2007 Thierry Vignaud <tv@mandriva.org> 1:1.0.15-1mdv2008.1
+ Revision: 98944
- new release

* Wed Aug 29 2007 Thierry Vignaud <tv@mandriva.org> 1:1.0.14-2mdv2008.0
+ Revision: 74634
- new devel policy (won't upgrade devel package due to circular obsolete but nothing relied on this devel package anyway...)
- fix file conflict
- fix man pages
- new release

* Thu May 03 2007 Thierry Vignaud <tv@mandriva.org> 1:1.0.14-0.rc4mdv2008.0
+ Revision: 21558
- new release

  + Adam Williamson <awilliamson@mandriva.org>
    - Import alsa-oss




* Thu Aug 24 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.0.12-1mdv2007.0
- new release

* Wed May 03 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.0.11-1mdk
- new release

* Fri Nov 04 2005 Thierry Vignaud <tvignaud@mandriva.com> 1.0.10-0.rc3.1mdk
- new release
- redo patch 0

* Mon May 09 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.9-0.rc3.1mdk
- new release

* Sat May 07 2005 Olivier Thauvin <nanardon@mandriva.org> 1.0.9-0.rc2.2mdk
- fix specfile

* Fri Apr 15 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.9-0.rc2.1mdk
- new release

* Mon Mar 21 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.8-2mdk
- fix requires

* Thu Jan 13 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.8-1mdk
- new release

* Fri Jan 07 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.8-0.rc2.1mdk
- new release

* Fri Nov 19 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.7-1mdk
- new release

* Mon Nov 15 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.6-2mdk
- patch 0: fix aoss script (#12281)
- fix requires and libification

* Mon Aug 16 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.6-1mdk
- new release

* Fri May 28 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.5-1mdk
- new release
- clean build

* Mon Apr 05 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.4-1mdk
- new release

* Tue Feb 24 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.2-3mdk
- fix changelog

* Tue Feb 24 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.2-2mdk
- fix unstallable package

* Fri Jan 09 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.1-1mdk
- new release

* Tue Aug 19 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.9.6-1mdk
- new release

* Wed Jul 16 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.9.0-0.8rc1mdk
- fix "let's obsolete myself" bug catched by distriblint

* Wed Jul 09 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.9.0-0.6rc1mdk
- fix provides/obsoletes conflict with libalsa2 (Andi Payn)

* Tue Apr 29 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.9.0-0.5rc1mdk
- fix buildrequires

* Fri Jan 03 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.9.0-0.4rc1mdk
- rebuild againts latest libalsa
- fix build with latest automake
- remove unpackaged static lib

* Thu Jul 18 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.9.0-0.3rc1mdk
- fix url

* Wed May 22 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.9.0-0.2rc1mdk
- build release

* Wed Apr 24 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.9.0-0.1rc1mdk
- release candidate 1

* Thu Apr 18 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.9.0-1beta11mdk
- initial release
