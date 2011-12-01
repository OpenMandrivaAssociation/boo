Summary: A wrist friendly language for the CLI/Mono
Name: boo
Version: 0.9.4.9
Release: 2
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
rm -rf %{buildroot}
nant -nologo install -D:install.prefix=%_prefix -D:install.destdir=%buildroot

rm -f %buildroot%{_datadir}/mime-info/boo.*

#gw fix pkgconfig location
%if %mdkversion >= 200600
mv %buildroot%_prefix/lib/pkgconfig %buildroot%_datadir/pkgconfig
%endif
rm -rf %buildroot%_datadir/gtksourceview*

%clean
rm -rf %{buildroot}

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
