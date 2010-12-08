Name: 	 	xpad
Summary: 	Sticky notepad for GTK+2
Version: 	4.0
Release: 	%mkrel 2
Source:		http://launchpad.net/xpad/trunk/%{version}/+download/%{name}-%{version}.tar.bz2
URL:		https://launchpad.net/xpad/
License:	GPLv3+
Group:		Office
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	gtk+2-devel >= 2.12
BuildRequires:	intltool

%description
Xpad is a GTK+2 application that emulates real-life sticky notes. If you
are likely to forget something, open up an xpad and jot it down. It
is easy-to-use, fault-tolerant, and its appearance is customizable.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%__rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%clean
%__rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README THANKS TODO ChangeLog
%{_bindir}/%name
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_mandir}/man1/*
