Summary: Statistics collection daemon for filling RRD files
Name: collectd
Version: 4.10.1
Release: 1%{?dist}
License: GPLv2
Group: System Environment/Daemons
URL: http://collectd.org/

Source: http://collectd.org/files/%{name}-%{version}.tar.gz
#Patch0: %{name}-4.9.1-include-collectd.d.patch
## bug 468067 "pkg-config --libs OpenIPMIpthread" fails
#Patch1: %{name}-4.6.2-configure-OpenIPMI.patch
## bug 564943 FTBFS system libiptc is not usable anymore, fix owniptc
#Patch2: libiptc-avoid-strict-aliasing-warnings.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libvirt-devel, libxml2-devel
BuildRequires: rrdtool-devel
BuildRequires: lm_sensors-devel
BuildRequires: curl-devel
%if 0%{?fedora} >= 8
BuildRequires: perl-libs, perl-devel
%else
BuildRequires: perl
%endif
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::Embed)
BuildRequires: net-snmp-devel
BuildRequires: libpcap-devel
BuildRequires: mysql-devel
BuildRequires: OpenIPMI-devel
BuildRequires: postgresql-devel
BuildRequires: nut-devel
BuildRequires: iptables-devel
BuildRequires: liboping-devel

%description
collectd is a small daemon written in C for performance.  It reads various
system  statistics  and updates  RRD files,  creating  them if necessary.
Since the daemon doesn't need to startup every time it wants to update the
files it's very fast and easy on the system. Also, the statistics are very
fine grained since the files are updated every 10 seconds.


%package apache
Summary:       Apache plugin for collectd
Group:         System Environment/Daemons
Requires:      collectd = %{version}-%{release}
%description apache
This plugin collects data provided by Apache's 'mod_status'.


%package dns
Summary:       DNS traffic analysis module for collectd
Group:         System Environment/Daemons
Requires:      collectd = %{version}-%{release}
%description dns
This plugin collects DNS traffic data.


%package email
Summary:       Email plugin for collectd
Group:         System Environment/Daemons
Requires:      collectd = %{version}-%{release}, spamassassin
%description email
This plugin collects data provided by spamassassin.


%package ipmi
Summary:       IPMI module for collectd
Group:         System Environment/Daemons
Requires:      collectd = %{version}-%{release}
%description ipmi
This plugin for collectd provides IPMI support.


%package mysql
Summary:       MySQL module for collectd
Group:         System Environment/Daemons
Requires:      collectd = %{version}-%{release}
%description mysql
MySQL querying plugin. This plugins provides data of issued commands,
called handlers and database traffic.


%package nginx
Summary:       Nginx plugin for collectd
Group:         System Environment/Daemons
Requires:      collectd = %{version}-%{release}
%description nginx
This plugin gets data provided by nginx.


%package nut
Summary:       Network UPS Tools module for collectd
Group:         System Environment/Daemons
Requires:      collectd = %{version}-%{release}
%description nut
This plugin for collectd provides Network UPS Tools support.


%package -n perl-Collectd
Summary:       Perl bindings for collectd
Group:         System Environment/Daemons
Requires:      collectd = %{version}-%{release}
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%description -n perl-Collectd
This package contains Perl bindings and plugin for collectd.


%package ping
Summary:       ping module for collectd
Group:         System Environment/Daemons
Requires:      collectd = %{version}-%{release}
%description ping
This plugin for collectd provides network latency statistics.


%package postgresql
Summary:       PostgreSQL module for collectd
Group:         System Environment/Daemons
Requires:      collectd = %{version}-%{release}
%description postgresql
PostgreSQL querying plugin. This plugins provides data of issued commands,
called handlers and database traffic.


%package rrdtool
Summary:       RRDTool module for collectd
Group:         System Environment/Daemons
Requires:      collectd = %{version}-%{release}, rrdtool
%description rrdtool
This plugin for collectd provides rrdtool support.


%package sensors
Summary:       Libsensors module for collectd
Group:         System Environment/Daemons
Requires:      collectd = %{version}-%{release}, lm_sensors
%description sensors
This plugin for collectd provides querying of sensors supported by
lm_sensors.


%package snmp
Summary:        SNMP module for collectd
Group:          System Environment/Daemons
Requires:       collectd = %{version}-%{release}, net-snmp
%description snmp
This plugin for collectd provides querying of net-snmp.


%package virt
Summary:       Libvirt plugin for collectd
Group:         System Environment/Daemons
Requires:      collectd = %{version}-%{release}
%description virt
This plugin collects information from virtualized guests.


%prep
%setup -q
#%patch0 -p1
#%patch1 -p0
#%patch2 -p1

sed -i.orig -e 's|-Werror||g' Makefile.in */Makefile.in


%build
%configure \
    --disable-ascent \
    --disable-static \
    --disable-ipvs \
    --enable-mysql \
    --enable-sensors \
    --enable-email \
    --enable-apache \
    --enable-perl \
    --enable-unixsock \
    --enable-ipmi \
    --enable-nut \
    --enable-postgresql \
    --enable-iptables \
    --enable-ping \
    --with-libiptc \
    --with-perl-bindings=INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__rm} -rf contrib/SpamAssassin
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0644 src/collectd.conf %{buildroot}%{_sysconfdir}/collectd.conf
%{__install} -Dp -m0755 contrib/fedora/init.d-collectd %{buildroot}%{_initrddir}/collectd

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/collectd/

# Convert docs to UTF-8
find contrib/ -type f -exec %{__chmod} a-x {} \;
for f in contrib/README ChangeLog ; do
  mv $f $f.old; iconv -f iso-8859-1 -t utf-8 < $f.old > $f; rm $f.old
done

# Remove Perl hidden .packlist files.
find %{buildroot} -name .packlist -exec rm {} \;
# Remove Perl temporary file perllocal.pod
find %{buildroot} -name perllocal.pod -exec rm {} \;

# Move the Perl examples to a separate directory.
mkdir perl-examples
find contrib -name '*.p[lm]' -exec mv {} perl-examples/ \;

# postresql config example will be included by %doc
rm %{buildroot}%{_datadir}/collectd/postgresql_default.conf

# Move config contribs
mkdir -p %{buildroot}/etc/collectd.d/
cp contrib/redhat/apache.conf %{buildroot}/etc/collectd.d/apache.conf
cp contrib/redhat/email.conf %{buildroot}/etc/collectd.d/email.conf
cp contrib/redhat/mysql.conf %{buildroot}/etc/collectd.d/mysql.conf
cp contrib/redhat/nginx.conf %{buildroot}/etc/collectd.d/nginx.conf
cp contrib/redhat/sensors.conf %{buildroot}/etc/collectd.d/sensors.conf
cp contrib/redhat/snmp.conf %{buildroot}/etc/collectd.d/snmp.conf

# configs for subpackaged plugins
for p in dns ipmi libvirt nut perl ping postgresql rrdtool
do
%{__cat} > %{buildroot}/etc/collectd.d/$p.conf <<EOF
LoadPlugin $p
EOF
done


# *.la files shouldn't be distributed.
rm -f %{buildroot}/%{_libdir}/{collectd/,}*.la


%post
/sbin/chkconfig --add collectd


%preun
if [ $1 -eq 0 ]; then
    /sbin/service collectd stop &>/dev/null || :
    /sbin/chkconfig --del collectd
fi


%postun
/sbin/service collectd condrestart &>/dev/null || :


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, -)

%config(noreplace) %{_sysconfdir}/collectd.conf
%config(noreplace) %{_sysconfdir}/collectd.d/
%exclude %{_sysconfdir}/collectd.d/apache.conf
%exclude %{_sysconfdir}/collectd.d/dns.conf
%exclude %{_sysconfdir}/collectd.d/email.conf
%exclude %{_sysconfdir}/collectd.d/ipmi.conf
%exclude %{_sysconfdir}/collectd.d/libvirt.conf
%exclude %{_sysconfdir}/collectd.d/mysql.conf
%exclude %{_sysconfdir}/collectd.d/nginx.conf
%exclude %{_sysconfdir}/collectd.d/nut.conf
%exclude %{_sysconfdir}/collectd.d/perl.conf
%exclude %{_sysconfdir}/collectd.d/ping.conf
%exclude %{_sysconfdir}/collectd.d/postgresql.conf
%exclude %{_sysconfdir}/collectd.d/rrdtool.conf
%exclude %{_sysconfdir}/collectd.d/sensors.conf
%exclude %{_sysconfdir}/collectd.d/snmp.conf

%{_initrddir}/collectd
%{_bindir}/collectd-nagios
%{_sbindir}/collectd
%{_sbindir}/collectdmon
%dir %{_localstatedir}/lib/collectd/

%dir %{_libdir}/collectd
%{_libdir}/collectd/apcups.so
%{_libdir}/collectd/battery.so
%{_libdir}/collectd/contextswitch.so
%{_libdir}/collectd/cpufreq.so
%{_libdir}/collectd/cpu.so
%{_libdir}/collectd/csv.so
%{_libdir}/collectd/df.so
%{_libdir}/collectd/disk.so
%{_libdir}/collectd/entropy.so
%{_libdir}/collectd/exec.so
%{_libdir}/collectd/filecount.so
%{_libdir}/collectd/hddtemp.so
%{_libdir}/collectd/interface.so
%{_libdir}/collectd/iptables.so
%{_libdir}/collectd/irq.so
%{_libdir}/collectd/load.so
%{_libdir}/collectd/logfile.so
%{_libdir}/collectd/madwifi.so
%{_libdir}/collectd/match_empty_counter.so
%{_libdir}/collectd/match_hashed.so
%{_libdir}/collectd/mbmon.so
%{_libdir}/collectd/memcached.so
%{_libdir}/collectd/memory.so
%{_libdir}/collectd/multimeter.so
%{_libdir}/collectd/network.so
%{_libdir}/collectd/nfs.so
%{_libdir}/collectd/ntpd.so
%{_libdir}/collectd/olsrd.so
%{_libdir}/collectd/powerdns.so
%{_libdir}/collectd/processes.so
%{_libdir}/collectd/serial.so
%{_libdir}/collectd/swap.so
%{_libdir}/collectd/syslog.so
%{_libdir}/collectd/tail.so
%{_libdir}/collectd/target_scale.so
%{_libdir}/collectd/tcpconns.so
%{_libdir}/collectd/teamspeak2.so
%{_libdir}/collectd/thermal.so
%{_libdir}/collectd/unixsock.so
%{_libdir}/collectd/users.so
%{_libdir}/collectd/uuid.so
%{_libdir}/collectd/vmem.so
%{_libdir}/collectd/vserver.so
%{_libdir}/collectd/wireless.so
%{_libdir}/collectd/write_http.so

%{_libdir}/collectd/bind.so
%{_libdir}/collectd/conntrack.so
%{_libdir}/collectd/curl.so
%{_libdir}/collectd/curl_xml.so
%{_libdir}/collectd/fscache.so
%{_libdir}/collectd/match_regex.so
%{_libdir}/collectd/match_timediff.so
%{_libdir}/collectd/match_value.so
%{_libdir}/collectd/openvpn.so
%{_libdir}/collectd/protocols.so
%{_libdir}/collectd/table.so
%{_libdir}/collectd/target_notification.so
%{_libdir}/collectd/target_replace.so
%{_libdir}/collectd/target_set.so
%{_libdir}/collectd/ted.so
%{_libdir}/collectd/uptime.so

%{_datadir}/collectd/types.db

# collectdclient - TBD reintroduce -devel subpackage?
%{_libdir}/libcollectdclient.so
%{_libdir}/libcollectdclient.so.0
%{_libdir}/libcollectdclient.so.0.0.0
%{_libdir}/pkgconfig/libcollectdclient.pc
%{_includedir}/collectd/client.h
%{_includedir}/collectd/lcc_features.h

%doc AUTHORS ChangeLog COPYING INSTALL README
%doc %{_mandir}/man1/collectd.1*
%doc %{_mandir}/man1/collectd-nagios.1*
%doc %{_mandir}/man1/collectdmon.1*
%doc %{_mandir}/man5/collectd.conf.5*
%doc %{_mandir}/man5/collectd-exec.5*
%doc %{_mandir}/man5/collectd-java.5*
%doc %{_mandir}/man5/collectd-unixsock.5*
%doc %{_mandir}/man5/collectd-python.5*
%doc %{_mandir}/man5/types.db.5*

%files apache
%defattr(-, root, root, -)
%{_libdir}/collectd/apache.so
%config(noreplace) %{_sysconfdir}/collectd.d/apache.conf


%files dns
%defattr(-, root, root, -)
%{_libdir}/collectd/dns.so
%config(noreplace) %{_sysconfdir}/collectd.d/dns.conf


%files email
%defattr(-, root, root, -)
%{_libdir}/collectd/email.so
%config(noreplace) %{_sysconfdir}/collectd.d/email.conf
%doc %{_mandir}/man5/collectd-email.5*


%files ipmi
%defattr(-, root, root, -)
%{_libdir}/collectd/ipmi.so
%config(noreplace) %{_sysconfdir}/collectd.d/ipmi.conf


%files mysql
%defattr(-, root, root, -)
%{_libdir}/collectd/mysql.so
%config(noreplace) %{_sysconfdir}/collectd.d/mysql.conf


%files nginx
%defattr(-, root, root, -)
%{_libdir}/collectd/nginx.so
%config(noreplace) %{_sysconfdir}/collectd.d/nginx.conf


%files nut
%defattr(-, root, root, -)
%{_libdir}/collectd/nut.so
%config(noreplace) %{_sysconfdir}/collectd.d/nut.conf


%files -n perl-Collectd
%defattr(-, root, root, -)
%doc perl-examples/*
%{_libdir}/collectd/perl.so
%{perl_vendorlib}/Collectd.pm
%{perl_vendorlib}/Collectd/
%config(noreplace) %{_sysconfdir}/collectd.d/perl.conf
%doc %{_mandir}/man5/collectd-perl.5*
%doc %{_mandir}/man3/Collectd::Unixsock.3pm*


%files ping
%defattr(-, root, root, -)
%{_libdir}/collectd/ping.so
%config(noreplace) %{_sysconfdir}/collectd.d/ping.conf


%files postgresql
%defattr(-, root, root, -)
%{_libdir}/collectd/postgresql.so
%config(noreplace) %{_sysconfdir}/collectd.d/postgresql.conf
%doc src/postgresql_default.conf


%files rrdtool
%defattr(-, root, root, -)
%{_libdir}/collectd/rrdtool.so
%config(noreplace) %{_sysconfdir}/collectd.d/rrdtool.conf


%files sensors
%defattr(-, root, root, -)
%{_libdir}/collectd/sensors.so
%config(noreplace) %{_sysconfdir}/collectd.d/sensors.conf


%files snmp
%defattr(-, root, root, -)
%{_libdir}/collectd/snmp.so
%config(noreplace) %{_sysconfdir}/collectd.d/snmp.conf
%doc %{_mandir}/man5/collectd-snmp.5*


%files virt
%defattr(-, root, root, -)
%{_libdir}/collectd/libvirt.so
%config(noreplace) %{_sysconfdir}/collectd.d/libvirt.conf


%changelog
* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 4.9.1-3
- Mass rebuild with perl-5.12.0

* Fri Mar 26 2010 Alan Pevec <apevec@redhat.com> 4.9.1-2
- enable ping plugin bz#541744

* Mon Mar 08 2010 Lubomir Rintel <lkundrak@v3.sl> 4.9.1-1
- New upstream version 4.9.1
  http://collectd.org/news.shtml#news81

* Tue Feb 16 2010 Alan Pevec <apevec@redhat.com> 4.8.3-1
- New upstream version 4.8.3
  http://collectd.org/news.shtml#news81
- FTBFS bz#564943 - system libiptc is not usable and owniptc fails to compile:
  add a patch from upstream iptables.git to fix owniptc compilation

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 4.8.1-3
- rebuild against perl 5.10.1

* Fri Nov 27 2009 Alan Pevec <apevec@redhat.com> 4.8.1-2
- use Fedora libiptc, owniptc in collectd sources fails to compile

* Wed Nov 25 2009 Alan Pevec <apevec@redhat.com> 4.8.1-1
- update to 4.8.1 (Florian La Roche) bz# 516276
- disable ping plugin until liboping is packaged bz# 541744

* Fri Sep 11 2009 Tom "spot" Callaway <tcallawa@redhat.com> 4.6.5-1
- update to 4.6.5
- disable ppc/ppc64 due to compile error

* Wed Sep 02 2009 Alan Pevec <apevec@redhat.com> 4.6.4-1
- fix condrestart: on upgrade collectd is not restarted, bz# 516273
- collectd does not re-connect to libvirtd, bz# 480997
- fix unpackaged files https://bugzilla.redhat.com/show_bug.cgi?id=516276#c4
- New upstream version 4.6.4
  http://collectd.org/news.shtml#news69

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 4.6.2-5
- rebuilt with new openssl

* Thu Aug  6 2009 Richard W.M. Jones <rjones@redhat.com> - 4.6.2-4
- Force rebuild to test FTBFS issue.
- lib/collectd/types.db seems to have moved to share/collectd/types.db

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 20 2009 Alan Pevec <apevec@redhat.com> 4.6.2-1
- New upstream version 4.6.2
  http://collectd.org/news.shtml#news64

* Tue Mar 03 2009 Alan Pevec <apevec@redhat.com> 4.5.3-2
- patch for strict-aliasing issue in liboping.c

* Mon Mar 02 2009 Alan Pevec <apevec@redhat.com> 4.5.3-1
- New upstream version 4.5.3
- fixes collectd is built without iptables plugin, bz# 479208
- list all expected plugins explicitly to avoid such bugs

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 4.5.1-3
- Rebuild against new mysql client.

* Sun Dec 07 2008 Alan Pevec <apevec@redhat.com> 4.5.1-2.1
- fix subpackages, bz# 475093

* Sun Nov 30 2008 Alan Pevec <apevec@redhat.com> 4.5.1-2
- workaround for https://bugzilla.redhat.com/show_bug.cgi?id=468067

* Sun Oct 22 2008 Alan Pevec <apevec@redhat.com> 4.5.1-1
- New upstream version 4.5.1, bz# 470943
  http://collectd.org/news.shtml#news59
- enable Network UPS Tools (nut) plugin, bz# 465729
- enable postgresql plugin
- spec cleanup, bz# 473641

* Fri Aug 01 2008 Alan Pevec <apevec@redhat.com> 4.4.2-1
- New upstream version 4.4.2.

* Thu Jul 03 2008 Lubomir Rintel <lkundrak@v3.sk> 4.4.1-4
- Fix a typo introduced by previous change that prevented building in el5

* Thu Jul 03 2008 Lubomir Rintel <lkundrak@v3.sk> 4.4.1-3
- Make this compile with older perl package
- Turn dependencies on packages to dependencies on Perl modules
- Add default attributes for files

* Wed Jun 12 2008 Alan Pevec <apevec@redhat.com> 4.4.1-2
- Split rrdtool into a subpackage (Chris Lalancette)
- cleanup subpackages, split dns plugin, enable ipmi
- include /etc/collectd.d (bz#443942)

* Mon Jun 09 2008 Alan Pevec <apevec@redhat.com> 4.4.1-1
- New upstream version 4.4.1.
- plugin changes: reenable iptables, disable ascent

* Tue May 27 2008 Alan Pevec <apevec@redhat.com> 4.4.0-2
- disable iptables/libiptc

* Mon May 26 2008 Alan Pevec <apevec@redhat.com> 4.4.0-1
- New upstream version 4.4.0.

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-9
- Added {?dist} to release number (thanks Alan Pevec).

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-8
- Bump release number so we can tag this in Rawhide.

* Thu Apr 17 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-6
- Exclude perl.so from the main package.

* Thu Apr 17 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-5
- Put the perl bindings and plugin into a separate perl-Collectd
  package.  Note AFAICT from the manpage, the plugin and Collectd::*
  perl modules must all be packaged together.

* Wed Apr 16 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-4
- Remove -devel subpackage.
- Add subpackages for apache, email, mysql, nginx, sensors,
  snmp (thanks Richard Shade).
- Add subpackages for perl, libvirt.

* Tue Apr 15 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-2
- Install Perl bindings in vendor dir not site dir.

* Tue Apr 15 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-1
- New upstream version 4.3.2.
- Create a -devel subpackage for development stuff, examples, etc.
- Use .bz2 package instead of .gz.
- Remove fix-hostname patch, now upstream.
- Don't mark collectd init script as config.
- Enable MySQL, sensors, email, apache, Perl, unixsock support.
- Don't remove example Perl scripts.
- Package types.db(5) manpage.
- Fix defattr.
- Build in koji to find the full build-requires list.

* Mon Apr 14 2008 Richard W.M. Jones <rjones@redhat.com> - 4.2.3.100.g79b0797-2
- Prepare for Fedora package review:
- Clarify license is GPLv2 (only).
- Setup should be quiet.
- Spelling mistake in original description fixed.
- Don't include NEWS in doc - it's an empty file.
- Convert some other doc files to UTF-8.
- config(noreplace) on init file.

* Thu Jan 10 2008 Chris Lalancette <clalance@redhat.com> - 4.2.3.100.g79b0797.1.ovirt
- Update to git version 79b0797
- Remove *.pm files so we don't get a bogus dependency
- Re-enable rrdtool; we will need it on the WUI side anyway

* Mon Oct 29 2007 Dag Wieers <dag@wieers.com> - 4.2.0-1 - 5946+/dag
- Updated to release 4.2.0.

* Mon Oct 29 2007 Dag Wieers <dag@wieers.com> - 3.11.5-1
- Initial package. (using DAR)
