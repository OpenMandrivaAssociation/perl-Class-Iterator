%define module Class-Iterator
%define name perl-%{module}
%define version 0.3
%define release %mkrel 5

Summary: 	A perl iterator class
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group: 		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Class/%{module}-%{version}.tar.gz
BuildArch:  noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_mandir}/*/*
%{perl_vendorlib}/*
