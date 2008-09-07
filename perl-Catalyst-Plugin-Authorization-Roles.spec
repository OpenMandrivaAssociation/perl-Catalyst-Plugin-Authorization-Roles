%define	module	Catalyst-Plugin-Authorization-Roles
%define	name	perl-%{module}
%define version 0.07
%define release %mkrel 1

%define _requires_exceptions perl(A

Summary:	Role based authorization for Catalyst based on Catalyst::Plugin::Authentication
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Catalyst/%{module}-%{version}.tar.gz
BuildRequires:	perl(Catalyst) >= 5.49
BuildRequires:	perl(Catalyst::Plugin::Authentication) >= 0.03
BuildRequires:	perl(Set::Object) >= 0
BuildRequires:	perl(Test::Exception) >= 0
BuildRequires:	perl(Test::MockObject) >= 1.01
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Role based access control is very simple: every user has a list of
roles, which that user is allowed to assume, and every restricted part
of the app makes an assertion about the necessary roles.

If the user is a member in all of the required roles access is
granted. Otherwise, access is denied.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL installdirs=vendor
%make

%check
make test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst

