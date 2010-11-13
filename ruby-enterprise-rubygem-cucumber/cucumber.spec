# Generated from cucumber-0.9.4.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(%{ruby} -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(%{ruby} -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname cucumber
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: cucumber-0.9.4
Name: ruby-enterprise-rubygem-%{gemname}
Version: 0.9.4
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://cukes.info
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby-enterprise-rubygems
Requires: ruby-enterprise-rubygem(gherkin) >= 2.2.9
Requires: ruby-enterprise-rubygem(term-ansicolor) >= 1.0.5
Requires: ruby-enterprise-rubygem(builder) >= 2.1.2
Requires: ruby-enterprise-rubygem(diff-lcs) >= 1.1.2
Requires: ruby-enterprise-rubygem(json) >= 1.4.6
Requires: ruby-enterprise-rubygem(rake) >= 0.8.7
Requires: ruby-enterprise-rubygem(rspec) >= 2.0.1
Requires: ruby-enterprise-rubygem(nokogiri) >= 1.4.3
Requires: ruby-enterprise-rubygem(prawn) = 0.8.4
Requires: ruby-enterprise-rubygem(prawn-layout) = 0.8.4
Requires: ruby-enterprise-rubygem(syntax) >= 1.0.0
Requires: ruby-enterprise-rubygem(spork) >= 0.8.4
BuildRequires: ruby-enterprise-rubygems
BuildArch: noarch
Provides: ruby-enterprise-rubygem(%{gemname}) = %{version}

%description
Behaviour Driven Development with elegance and joy

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
%{_bindir}/cucumber
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/History.txt
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Sat Nov 13 2010 Roberto Gaiser <rgaiser@shrek.intranet> - 0.9.4-1
- Initial package
