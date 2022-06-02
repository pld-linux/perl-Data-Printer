#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Data
%define		pnam	Printer
Summary:	Data::Printer - colored pretty-print of Perl data structures and objects
Summary(pl.UTF-8):	Data::Printer - kolorowe, ładne wypisywanie perlowych struktur danych i obiektów
Name:		perl-Data-Printer
Version:	1.000004
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Data/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	34e52ee70a7a19779251062251f6f422
URL:		https://metacpan.org/dist/Data-Printer
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Package-Stash >= 0.3
BuildRequires:	perl-Scalar-List-Utils
BuildRequires:	perl-Sort-Key
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-version >= 0.77
%endif
Suggests:	perl-Sort-Key
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Colored pretty-print of Perl data structures and objects.

%description -l pl.UTF-8
Kolorowe, ładne wypisywanie perlowych struktur danych i obiektów.

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
%{perl_vendorlib}/Data/Printer.pm
%{perl_vendorlib}/Data/Printer
%{_mandir}/man3/DDP.3pm*
%{_mandir}/man3/Data::Printer*.3pm*
%{_examplesdir}/%{name}-%{version}
