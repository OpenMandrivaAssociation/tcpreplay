Summary:	A tool to replay captured network traffic
Name:		tcpreplay
Version:	3.2.1
Release:	%mkrel 1
License:	BSD
Group:		Networking/Other
URL:		http://tcpreplay.sf.net/
Source0:	http://prdownloads.sourceforge.net/tcpreplay/%{name}-%{version}.tar.gz
BuildRequires:	tcpdump
BuildRequires:	libpcap-devel >= 0.7.2
BuildRequires:	autogen-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Tcpreplay is a tool to replay captured network traffic. Currently, tcpreplay
supports pcap (tcpdump) and snoop capture formats. Also included, is tcpprep a
tool to pre-process capture files to allow increased performance under certain
conditions as well as capinfo which provides basic information about capture
files.

%prep

%setup -q

%build

%configure2_5x

# build against the shared build deps
find -name "Makefile" | xargs perl -pi -e "s|^LPCAPLIB.*|LPCAPLIB = -lpcap|g"
find -name "Makefile" | xargs perl -pi -e "s|%{_libdir}/libpcap\.a|-lpcap|g"

%make

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
