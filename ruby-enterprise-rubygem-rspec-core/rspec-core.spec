# Generated from rspec-core-2.1.0.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(%{ruby} -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(%{ruby} -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname rspec-core
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: rspec-core-2.1.0
Name: ruby-enterprise-rubygem-%{gemname}
Version: 2.1.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/rspec/rspec-core
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby-enterprise-rubygems
BuildRequires: ruby-enterprise-rubygems
BuildArch: noarch
Provides: ruby-enterprise-rubygem(%{gemname}) = %{version}

%description
RSpec runner and example groups

%prep

if ! [ -e %{ruby} ]; then
    echo "Please provide your ruby enterprise path"
    echo "%{ruby} does not exists"
    echo "Use: --define 'ruby ruby path'"
    exit 1
fi

rubyrpm=`rpm -q --whatprovides %{ruby}`

if ! [[ $rubyrpm =~ ^ruby-enterprise ]]; then
    echo "Please provide your ruby enterprise path"
    echo "%{ruby} it's not from the ruby-enterprise RPM"
    echo "Use: --define 'ruby ruby path'"
    exit 1
fi

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
%{_bindir}/autospec
%{_bindir}/rspec
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README.markdown
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Fri Nov 12 2010 Roberto Gaiser <rgaiser@optimus.local> - 2.1.0-1
- Initial package
