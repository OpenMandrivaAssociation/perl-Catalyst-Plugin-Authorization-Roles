%define	upstream_name	 Catalyst-Plugin-Authorization-Roles
%define upstream_version 0.09

%define _requires_exceptions perl(A

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Role based authorization for Catalyst based on Catalyst::Plugin::Authentication
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Catalyst) >= 5.49
BuildRequires:	perl(Catalyst::Plugin::Authentication) >= 0.03
BuildRequires:	perl(Set::Object) >= 0
BuildRequires:	perl(Test::Exception) >= 0
BuildRequires:	perl(Test::MockObject) >= 1.01
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Role based access control is very simple: every user has a list of
roles, which that user is allowed to assume, and every restricted part
of the app makes an assertion about the necessary roles.

If the user is a member in all of the required roles access is
granted. Otherwise, access is denied.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
