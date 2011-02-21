# Assuming you are building a full RPM based environment,
# this spec assumes you have Ruby 1.9.2 and RubyGems 1.5.0 packages already installed.

%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname bundler
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: The best way to manage your application's dependencies
Name: rubygem-%{gemname}
Version: 1.0.10
Release: 1%{?dist}
Group: Development/Libraries
License: GPLv2+ or Ruby
URL: http://gembundler.com
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby >= 1.9.2 rubygems >= 1.5.0
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Bundler manages an application's dependencies through its entire life, across
many machines, systematically and repeatably

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/bundle
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%changelog
* Fri Feb 18 2011 Caio Filipini <caiofilipini@gmail.com>
- Bundler version 1.0.10

