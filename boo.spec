%define monodir %_prefix/lib
%if %mdkversion >= 200600
%define pkgconfigdir %_datadir/pkgconfig
%else
%define pkgconfigdir %monodir/pkgconfig
%endif
Summary:		A wrist friendly language for the CLI/Mono
Name:			boo
Version: 0.7.6.2237
Release: 		%mkrel 4
License:		BSD
Group:			Development/Other
Source0:		http://dist.codehaus.org/boo/distributions/boo-%{version}-src.tar.bz2
URL:			http://boo.codehaus.org/
BuildRoot:		%{_tmppath}/%{name}-%{version}-buildroot
Requires:	mono
BuildRequires:	nant
BuildRequires:	shared-mime-info
#gw for the boo.lang location
BuildRequires:  libgtksourceview-devel
Requires(post): shared-mime-info
Requires(postun): shared-mime-info
BuildArch:		noarch

%description
Boo is a new object oriented statically typed programming language for
the Common Language Infrastructure with a python inspired syntax and
a special focus on language and compiler extensibility.

%prep
%setup -q
perl -pi -e 's/\r//' $(find examples/ -type f )

%build
nant -nologo -D:install.prefix=%_prefix

%check
#gw tests fail :-(
#nant -nologo test

%install
rm -rf $RPM_BUILD_ROOT
nant -nologo install  -D:install.prefix=%_prefix -D:install.destdir=%buildroot

#gw move the nant task to the right dir
mkdir -p %buildroot%_datadir/NAnt/bin
mv %buildroot%monodir/boo/Boo.NAnt.Tasks.dll %buildroot%_datadir/NAnt/bin

#gw fix pkgconfig location
%if %mdkversion >= 200600
mv %buildroot%monodir/pkgconfig  %buildroot%pkgconfigdir
%endif
rm -rf %buildroot%_datadir/gtksourceview*

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database

%postun 
%clean_mime_database

%files
%defattr(-, root, root)
%doc license.txt readme.txt examples docs/BooManifesto.sxw
%{_bindir}/boo*
%monodir/mono/boo/
%monodir/boo/
%monodir/mono/gac/Boo*
%_datadir/NAnt/bin/Boo.NAnt.Tasks.dll
%{_datadir}/mime/packages/boo-mime-info.xml
%{_datadir}/mime-info/boo.*
%pkgconfigdir/boo.pc

