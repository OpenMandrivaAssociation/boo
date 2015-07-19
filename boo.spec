Summary:	A wrist friendly language for the CLI/Mono
Name:		boo
Version:	0.9.4.9
Release:	10
License:	BSD
Group:		Development/Other
Url:		http://boo.codehaus.org/
Source0:	http://dist.codehaus.org/boo/distributions/%{name}-%{version}-src.tar.bz2
Source100:  %{name}.rpmlintrc
Patch0:		boo-gtksourceview.patch
Patch1:		boo-pkgconfig_path_fix.patch
BuildArch:	noarch

BuildRequires:	nant
BuildRequires:	shared-mime-info
BuildRequires:	pkgconfig(gtksourceview-2.0)
BuildRequires:	mono
BuildRequires:	pkgconfig(mono)
BuildRequires:	pkgconfig(shared-mime-info)
Requires:	mono

%description
Boo is a new object oriented statically typed programming language for
the Common Language Infrastructure with a python inspired syntax and
a special focus on language and compiler extensibility.

%package	nant
Summary:	Nant task for building boo programs
Group:		Development/Other

%description	nant
Boo is a new object oriented statically typed programming language for
the Common Language Infrastructure with a python inspired syntax and
a special focus on language and compiler extensibility.

This is a Nant task for building boo sources.

%prep
%setup -q
%apply_patches

%build
nant -nologo -D:install.prefix=%{_prefix}

%install
nant -nologo install -D:install.prefix=%{_prefix} -D:install.destdir=%{buildroot}

rm -f %{buildroot}%{_datadir}/mime-info/boo.*

#gw fix pkgconfig location
mv %{buildroot}%{_prefix}/lib/pkgconfig %{buildroot}%{_datadir}/pkgconfig

rm -rf %{buildroot}%{_datadir}/gtksourceview*

%files
%doc license.txt readme.txt examples docs/BooManifesto.sxw
%{_bindir}/boo*
%{_prefix}/lib/mono/*
%{_prefix}/lib/boo
%{_datadir}/mime/packages/boo-mime-info.xml
%{_datadir}/pkgconfig/boo.pc
%exclude %{_prefix}/lib/boo/Boo.NAnt.Tasks.dll

%files nant
%{_prefix}/lib/boo/Boo.NAnt.Tasks.dll

