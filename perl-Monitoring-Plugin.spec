#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	Monitoring
%define	pnam	Plugin
Summary:	Monitoring::Plugin - A family of Perl modules to streamline writing Monitoring plugins
Summary(pl.UTF-8):	Monitoring::Plugin - rodzina modułów Perla ułatwiająca pisanie wtyczek Monitoringa
Name:		perl-Monitoring-Plugin
Version:	0.39
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/N/NI/NIERLEIN/Monitoring-Plugin-%{version}.tar.gz
# Source0-md5:	c786ada6289bda2c4380d3df3b5185d5
URL:		http://search.cpan.org/dist/Monitoring-Plugin/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::More) >= 0.62
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-Config-Tiny
BuildRequires:	perl-Math-Calc-Units
BuildRequires:	perl-Params-Validate
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Monitoring::Plugin and its associated Monitoring::Plugin::* modules
are a family of Perl modules to streamline writing Monitoring plugins.
The main end user modules are Monitoring::Plugin, providing an
object-oriented interface to the entire Monitoring::Plugin::*
collection, and Monitoring::Plugin::Functions, providing a simpler
functional interface to a useful subset of the available
functionality.

The purpose of the collection is to make it as simple as possible for
developers to create plugins that conform the Monitoring Plugin
guidelines <https://www.monitoring-plugins.org/doc/guidelines.html>.

%description -l pl.UTF-8
Monitoring::Plugin i związane z nim moduły Monitoring::Plugin::* to
rodzina modułów Perla ułatwiająca pisanie wtyczek Monitoringa. Główne
moduły dla użytkownika końcowego to Monitoring::Plugin, udostępniający
zorientowany obiektowo interfejs do całej kolekcji
Monitoring::Plugin::*, oraz Monitoring::Plugin::Functions,
udostępniający prostszy, funkcyjny interfejs do przydatnego podzbioru
dostępnej funkcjonalności.

Celem tej kolekcji jest jak największe ułatwienie programistom
tworzenia wtyczek zgodnych z zaleceniami dla wtyczek Monitoringa:
<https://www.monitoring-plugins.org/doc/guidelines.html>.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p t/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Monitoring
%{perl_vendorlib}/Monitoring/*.pm
%{perl_vendorlib}/Monitoring/Plugin
%{_mandir}/man3/Monitoring::Plugin*.3pm*
%{_examplesdir}/%{name}-%{version}
