%define	upstream_name	 Catalyst-Plugin-Authorization-Roles
%define upstream_version 0.09

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(A(.*)\\)'
%else
%define _requires_exceptions perl(A
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Role based authorization for Catalyst based on Catalyst::Plugin::Authentication
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst) >= 5.49
BuildRequires:	perl(Catalyst::Plugin::Authentication) >= 0.03
BuildRequires:	perl(Set::Object) >= 0
BuildRequires:	perl(Test::Exception) >= 0
BuildRequires:	perl(Test::MockObject) >= 1.01
BuildArch:	noarch

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
%makeinstall_std

%files
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst


%changelog
* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 662008
- update to new version 0.09

* Sat Nov 21 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 467874
- update to 0.08

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 406260
- rebuild using %%perl_convert_version

* Sun Sep 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2009.0
+ Revision: 282125
- new version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.05-3mdv2009.0
+ Revision: 241160
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Apr 30 2007 Olivier Thauvin <nanardon@mandriva.org> 0.05-1mdv2008.0
+ Revision: 19680
- fix build method

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    -New version


* Wed Mar 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdk
- new version 
- rpmbuilupdate aware
- fix directory ownership

* Wed Jan 18 2006 Scott Karns <scott@karnstech.com> 0.03-1mdk
- Initial MDV package

