Summary: A wrist friendly language for the CLI/Mono
Name: boo
Version: 0.9.4.9
Release: %mkrel 2
License: BSD
Group: Development/Other
Source0: http://dist.codehaus.org/boo/distributions/boo-%{version}-src.tar.bz2
Patch0: boo-gtksourceview.patch
Patch1: boo-pkgconfig_path_fix.patch
URL: http://boo.codehaus.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: mono
BuildRequires: nant
BuildRequires: shared-mime-info
BuildRequires: libgtksourceview-2.0-devel
BuildConflicts: boo < %version
BuildArch: noarch

%description
Boo is a new object oriented statically typed programming language for
the Common Language Infrastructure with a python inspired syntax and
a special focus on language and compiler extensibility.

%package nant
Summary: Nant task for building boo programs
Group: Development/Other

%description nant
Boo is a new object oriented statically typed programming language for
the Common Language Infrastructure with a python inspired syntax and
a special focus on language and compiler extensibility.

This is a Nant task for building boo sources.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
nant -nologo -D:install.prefix=%_prefix

%install
rm -rf $RPM_BUILD_ROOT
nant -nologo install -D:install.prefix=%_prefix -D:install.destdir=%buildroot

rm -f %buildroot%{_datadir}/mime-info/boo.*

#gw fix pkgconfig location
%if %mdkversion >= 200600
mv %buildroot%_prefix/lib/pkgconfig %buildroot%_datadir/pkgconfig
%endif
rm -rf %buildroot%_datadir/gtksourceview*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc license.txt readme.txt examples docs/BooManifesto.sxw
%{_bindir}/boo*
%{_prefix}/lib/mono/*
%{_prefix}/lib/boo
%{_datadir}/mime/packages/boo-mime-info.xml
%{_datadir}/pkgconfig/boo.pc
%exclude %{_prefix}/lib/boo/Boo.NAnt.Tasks.dll

%files nant
%defattr(-, root, root)
%{_prefix}/lib/boo/Boo.NAnt.Tasks.dll


%changelog
* Sun May 01 2011 Funda Wang <fwang@mandriva.org> 0.9.4.9-1mdv2011.0
+ Revision: 661239
- new version 0.9.4.9

* Thu Oct 07 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.3-1mdv2011.0
+ Revision: 583938
- new version
- drop patch 3

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.2-3mdv2010.1
+ Revision: 522255
- rebuilt for 2010.1

* Wed Sep 02 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.2-2mdv2010.0
+ Revision: 424071
- fix path in wrapper scripts

* Tue Sep 01 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.2-1mdv2010.0
+ Revision: 423819
- new version

* Mon Jul 13 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.1-1mdv2010.0
+ Revision: 395443
- new version
- update patch 0

* Tue Jan 27 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.0-1mdv2009.1
+ Revision: 334207
- new version
- rediff patch 0

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 0.8.2-3mdv2009.0
+ Revision: 264329
- rebuild early 2009.0 package (before pixel changes)

* Wed May 21 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.8.2-2mdv2009.0
+ Revision: 209681
- new version

* Thu May 08 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.8.1-2mdv2009.0
+ Revision: 204460
- move nant support to a subpackage

* Sun Feb 10 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.8.1-1mdv2008.1
+ Revision: 164981
- new version
- rediff patch 0

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.8.0-2mdv2008.1
+ Revision: 133601
- rebuild for new nant

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Oct 25 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.8.0-1mdv2008.1
+ Revision: 102158
- new version

* Sun Sep 02 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.7.9.2659-2mdv2008.0
+ Revision: 78355
- fix pkgconfig file

* Sun Sep 02 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.7.9.2659-1mdv2008.0
+ Revision: 78231
- new version
- build conflict with old boo

* Tue Jun 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.7.8.2559-1mdv2008.0
+ Revision: 38235
- fix build
- new version

* Mon May 07 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.7.7.2475-1mdv2008.0
+ Revision: 24625
- new version
- fix build


* Tue Oct 17 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.7.6.2237-4mdv2007.1
- - rebuild for new nant

* Thu Jul 27 2006 Götz Waschk <waschk@mandriva.org> 0.7.6.2237-3mdv2007.0
- rebuild for new find-requires
- readd buildrequires for gtksourceview

* Wed Jul 26 2006 Götz Waschk <waschk@mandriva.org> 0.7.6.2237-2mdv2007.0
- remove gtksourceview language file

* Wed Jun 28 2006 Götz Waschk <waschk@mandriva.org> 0.7.6.2237-1mdv2007.0
- use new macros
- New release 0.7.6.2237

* Wed Jun 07 2006 Götz Waschk <waschk@mandriva.org> 0.7.5.2013-2mdv2007.0
- rebuild for new nant

* Mon Dec 12 2005 Götz Waschk <waschk@mandriva.org> 0.7.5.2013-1mdk
- new version

* Fri Oct 21 2005 Götz Waschk <waschk@mandriva.org> 0.7.0.1921-1mdk
- fix postin/un deps
- New release 0.7.0.1921

* Fri Sep 02 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.6.0.1858-1mdk
- New release 0.6.0.1858

* Fri Jul 01 2005 Götz Waschk <waschk@mandriva.org> 0.5.6.1701-1mdk
- New release 0.5.6.1701

* Wed Jun 01 2005 Götz Waschk <waschk@mandriva.org> 0.5.5.1651-1mdk
- New release 0.5.5.1651

* Wed May 25 2005 Götz Waschk <waschk@mandriva.org> 0.5.4.1629-3mdk
- fix buildrequires

* Wed May 25 2005 Götz Waschk <waschk@mandriva.org> 0.5.4.1629-2mdk
- fix build on x86_64 hosts
- fix buildrequires

* Tue May 24 2005 Götz Waschk <waschk@mandriva.org> 0.5.4.1629-1mdk
- New release 0.5.4.1629

* Tue May 24 2005 Götz Waschk <waschk@mandriva.org> 0.5.3.1544-3mdk
- move the nant task to the right directory

* Sat May 21 2005 Götz Waschk <waschk@mandriva.org> 0.5.3.1544-2mdk
- let nant do the install stuff
- add missing pkgconfig file

* Sat May 21 2005 Götz Waschk <waschk@mandriva.org> 0.5.3.1544-1mdk
- %%_libdir in noarch no good
- use the sources
- new version

* Thu Apr 28 2005 Michael Scherer <misc@mandriva.org> 0.5.2-1mdk
- from Tigrux <tigrux@ximian.com>
  - First rpm for Mandriva

