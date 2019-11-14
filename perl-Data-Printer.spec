#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Data
%define		pnam	Printer
%include	/usr/lib/rpm/macros.perl
Summary:	Data::Printer - colored pretty-print of Perl data structures and objects
#Summary(pl.UTF-8):	
Name:		perl-Data-Printer
Version:	0.40
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/G/GA/GARU/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a8d976880254233775bba35b2989b61c
URL:		http://search.cpan.org/dist/Data-Printer/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Clone::PP)
BuildRequires:	perl(File::HomeDir) >= 0.91
BuildRequires:	perl(Sort::Naturally)
BuildRequires:	perl-Package-Stash >= 0.3
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Colored pretty-print of Perl data structures and objects.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%{perl_vendorlib}/DDP.pm
%{perl_vendorlib}/Data/*.pm
%{perl_vendorlib}/Data/Printer
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
