%define module Class-Iterator
%define name perl-%{module}
%define version 0.3
%define release %mkrel 2

Summary: 	A perl iterator class
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group: 		Development/Perl
Source: 	http://search.cpan.org/CPAN/authors/id/T/TE/TEXMEC/%{module}-%{version}.tar.gz
Url: 		http://www.cpan.org
BuildRequires: perl-devel
BuildArch: noarch

%description
Class::Iterator is a generic iterator object class. It use a closure an
wrap into an object interface.

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_mandir}/*/*
%{perl_vendorlib}/*


* Thu Jun 16 2005 Olivier Thauvin <nanardon@mandriva.org> 0.3-1mdk
- first mdk release
