Summary:	A tool to replay captured network traffic
Name:		tcpreplay
Version:	3.4.4
Release:	3
License:	BSD
Group:		Networking/Other
URL:		http://tcpreplay.synfin.net/trac/
Source0:	http://prdownloads.sourceforge.net/tcpreplay/%{name}-%{version}.tar.gz
Patch0:		tcpreplay-3.4.2-get_interface.patch
BuildRequires:	autogen >= 5.9
BuildRequires:	autogen-devel >= 5.9
BuildRequires:	libdnet-devel
BuildRequires:	libpcap-devel >= 0.7.2
BuildRequires:	tcpdump
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Tcpreplay is a tool to replay captured network traffic. Currently, tcpreplay
supports pcap (tcpdump) and snoop capture formats. Also included, is tcpprep a
tool to pre-process capture files to allow increased performance under certain
conditions as well as capinfo which provides basic information about capture
files.

%prep
%setup -q
%patch0 -p1 -b .get_interface

%build
%configure2_5x \
    --enable-dynamic-link \
    --enable-tcpreplay-edit \
    --with-testnic=eth0 \
    --with-testnic2=eth1
%make

#%%check
#make test <- requires root permissions

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README docs/CHANGELOG docs/CREDIT docs/HACKING docs/INSTALL docs/LICENSE docs/TODO
%{_bindir}/tcpbridge
%{_bindir}/tcpprep
%{_bindir}/tcpreplay
%{_bindir}/tcpreplay-edit
%{_bindir}/tcprewrite
%{_mandir}/man1/*


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 3.4.4-2mdv2011.0
+ Revision: 615167
- the mass rebuild of 2010.1 packages

* Fri Apr 23 2010 Sandro Cazzaniga <kharec@mandriva.org> 3.4.4-1mdv2010.1
+ Revision: 538158
- update to 3.4.4

* Sat Jun 27 2009 Frederik Himpe <fhimpe@mandriva.org> 3.4.3-1mdv2010.0
+ Revision: 389595
- update to new version 3.4.3

* Tue Jun 16 2009 Wanderlei Cavassin <cavassin@mandriva.com.br> 3.4.2-2mdv2010.0
+ Revision: 386236
- fix parsing of interface name

* Thu May 21 2009 Oden Eriksson <oeriksson@mandriva.com> 3.4.2-1mdv2010.0
+ Revision: 378419
- 3.4.2
- 3.4.1

* Thu Jan 15 2009 Oden Eriksson <oeriksson@mandriva.com> 3.4.0-1mdv2009.1
+ Revision: 329715
- 3.4.0

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 3.3.2-2mdv2009.1
+ Revision: 298408
- rebuilt against libpcap-1.0.0

* Sun Jun 22 2008 Oden Eriksson <oeriksson@mandriva.com> 3.3.2-1mdv2009.0
+ Revision: 227869
- 3.3.2
- fix deps

* Sun May 18 2008 Oden Eriksson <oeriksson@mandriva.com> 3.3.1-1mdv2009.0
+ Revision: 208629
- 3.3.1

* Tue May 06 2008 Oden Eriksson <oeriksson@mandriva.com> 3.3.0-0mdv2009.0
+ Revision: 201829
- 3.3.0

* Fri Jan 25 2008 Oden Eriksson <oeriksson@mandriva.com> 3.2.5-1mdv2008.1
+ Revision: 157843
- 3.2.5

* Thu Jan 17 2008 Oden Eriksson <oeriksson@mandriva.com> 3.2.4-1mdv2008.1
+ Revision: 154131
- 3.2.4

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 26 2007 Oden Eriksson <oeriksson@mandriva.com> 3.2.1-1mdv2008.1
+ Revision: 102320
- 3.2.1

* Tue Aug 28 2007 Oden Eriksson <oeriksson@mandriva.com> 3.2.0-1mdv2008.0
+ Revision: 72646
- 3.2.0

* Fri Jul 20 2007 Oden Eriksson <oeriksson@mandriva.com> 3.1.1-1mdv2008.0
+ Revision: 53879
- 3.1.1

* Wed May 02 2007 Oden Eriksson <oeriksson@mandriva.com> 3.0.1-1mdv2008.0
+ Revision: 20475
- 3.0.1

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-1mdv2008.0
+ Revision: 16072
- fix deps
- 3.0.0


* Tue Jul 18 2006 Stefan van der Eijk <stefan@mandriva.org> 2.3.5-4
- rebuild
- %%mkrel

* Fri Mar 17 2006 Oden Eriksson <oeriksson@mandriva.com> 2.3.5-3mdk
- rebuilt against libnet1.1.2

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 2.3.5-2mdk
- rebuilt against new libpcap-0.9.1 (aka. a "play safe" rebuild)

* Mon Jul 04 2005 Oden Eriksson <oeriksson@mandriva.com> 2.3.5-1mdk
- 2.3.5

* Fri Feb 11 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.3.3-1mdk
- 2.3.3
- fix deps

* Mon Nov 08 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.3.2-1mdk
- 2.3.2
- fix deps

* Mon Sep 27 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.3.1-1mdk
- 2.3.1

* Mon Sep 06 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.3.0-1mdk
- 2.3.0
- build against the new shared libnet2

* Tue Jun 22 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.2.2-1mdk
- 2.2.2

* Sun May 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.2.0-1mdk
- 2.2.0
- fix P0
- fix deps

* Sun Dec 07 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.4.6-1mdk
- 1.4.6

* Sat Aug 30 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.4.5-1mdk
- 1.4.5

* Wed Aug 13 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.4.4-1mdk
- 1.4.4

