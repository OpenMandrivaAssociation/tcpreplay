Summary:	A tool to replay captured network traffic
Name:		tcpreplay
Version:	3.3.0
Release:	%mkrel 0
License:	BSD
Group:		Networking/Other
URL:		http://tcpreplay.synfin.net/trac/
Source0:	http://prdownloads.sourceforge.net/tcpreplay/%{name}-%{version}.tar.gz
BuildRequires:	autogen-devel
BuildRequires:	libdnet-devel
BuildRequires:	libpcap-devel >= 0.7.2
BuildRequires:	tcpdump
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Tcpreplay is a tool to replay captured network traffic. Currently, tcpreplay
supports pcap (tcpdump) and snoop capture formats. Also included, is tcpprep a
tool to pre-process capture files to allow increased performance under certain
conditions as well as capinfo which provides basic information about capture
files.

%prep

%setup -q

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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README docs/CHANGELOG docs/CREDIT docs/HACKING docs/INSTALL docs/LICENSE docs/TODO
%{_bindir}/tcpbridge
%{_bindir}/tcpprep
%{_bindir}/tcpreplay
%{_bindir}/tcprewrite
%{_mandir}/man1/*
