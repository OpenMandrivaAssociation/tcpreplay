%define name	tcpreplay
%define version	2.3.5
%define release	%mkrel 4

Summary:	A tool to replay captured network traffic
Name:		%{name}
Version:	%{version} 
Release:	%{release} 
License:	BSD
Group:		Networking/Other
URL:		http://tcpreplay.sf.net/
Source0:	http://prdownloads.sourceforge.net/tcpreplay/%{name}-%{version}.tar.bz2
Patch0:		tcpreplay-2.2.0-DESTDIR.patch
BuildRequires:	tcpdump
BuildRequires:	libnet1.1.2-devel
BuildRequires:	libpcap-devel >= 0.7.2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Tcpreplay is a tool to replay captured network traffic. Currently,
tcpreplay supports pcap (tcpdump) and snoop capture formats. Also
included, is tcpprep a tool to pre-process capture files to allow
increased performance under certain conditions as well as capinfo
which provides basic information about capture files.

%prep

%setup -q
%patch0 -p0 -b .DESTDIR

%build

%configure2_5x

%make CFLAGS="%{optflags}"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Docs/CHANGELOG Docs/CREDIT Docs/*.css Docs/*.html Docs/*.png
%doc Docs/*.pdf Docs/*.txt Docs/TODO Docs/HACKING Docs/LICENSE
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man8/*
%{_mandir}/man1/*

