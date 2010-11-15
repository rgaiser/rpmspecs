# Generated from commander-4.0.3.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(%{ruby} -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(%{ruby} -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname commander
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: The complete solution for Ruby command-line executables
Name: ruby-enterprise-rubygem-%{gemname}
Version: 4.0.3
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://visionmedia.github.com/commander
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby-enterprise-rubygems
Requires: ruby-enterprise-rubygem(highline) >= 1.5.0
BuildRequires: ruby-enterprise-rubygems
BuildArch: noarch
Provides: ruby-enterprise-rubygem(%{gemname}) = %{version}

%description
The complete solution for Ruby command-line executables

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
%{_bindir}/commander
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/bin/commander
%doc %{geminstdir}/lib/commander.rb
%doc %{geminstdir}/lib/commander/blank.rb
%doc %{geminstdir}/lib/commander/command.rb
%doc %{geminstdir}/lib/commander/core_ext.rb
%doc %{geminstdir}/lib/commander/core_ext/array.rb
%doc %{geminstdir}/lib/commander/core_ext/object.rb
%doc %{geminstdir}/lib/commander/delegates.rb
%doc %{geminstdir}/lib/commander/help_formatters.rb
%doc %{geminstdir}/lib/commander/help_formatters/base.rb
%doc %{geminstdir}/lib/commander/help_formatters/terminal.rb
%doc %{geminstdir}/lib/commander/help_formatters/terminal/command_help.erb
%doc %{geminstdir}/lib/commander/help_formatters/terminal/help.erb
%doc %{geminstdir}/lib/commander/help_formatters/terminal_compact.rb
%doc %{geminstdir}/lib/commander/help_formatters/terminal_compact/command_help.erb
%doc %{geminstdir}/lib/commander/help_formatters/terminal_compact/help.erb
%doc %{geminstdir}/lib/commander/import.rb
%doc %{geminstdir}/lib/commander/platform.rb
%doc %{geminstdir}/lib/commander/runner.rb
%doc %{geminstdir}/lib/commander/user_interaction.rb
%doc %{geminstdir}/lib/commander/version.rb
%doc %{geminstdir}/tasks/docs.rake
%doc %{geminstdir}/tasks/gemspec.rake
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon Nov 15 2010 Roberto Gaiser <rgaiser@shrek.intranet> - 4.0.3-1
- Initial package
