%define name	xpad
%define version	2.13
%define release %mkrel 1
%define icon48	%_builddir/%{name}-%{version}/images/hicolor/48x48/apps/%{name}.png

Name: 	 	%{name}
Summary: 	Sticky notepad for GTK+2
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/xpad/%{name}-%{version}.tar.bz2
#Source1: 	%{name}48.png
Source2: 	%{name}32.png
Source3: 	%{name}16.png
URL:		http://xpad.sourceforge.net
License:	GPLv2+
Requires:	gtk+2.0 >= 2.6
Group:		Office
BuildRequires:	pkgconfig gtk+2-devel >= 2.6 gettext

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
%makeinstall

%find_lang %name

#icons
%__mkdir -p $RPM_BUILD_ROOT%_liconsdir
%__cp %{icon48} $RPM_BUILD_ROOT%_liconsdir/%{name}.png
#%__cat %SOURCE1 > $RPM_BUILD_ROOT/%_liconsdir/%name.png
%__mkdir -p $RPM_BUILD_ROOT%_iconsdir
%__cat %SOURCE2 > $RPM_BUILD_ROOT%_iconsdir/%name.png
%__mkdir -p $RPM_BUILD_ROOT%_miconsdir
%__cat %SOURCE3 > $RPM_BUILD_ROOT%_miconsdir/%name.png


%clean
%__rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README THANKS TODO ChangeLog
%{_bindir}/%name
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_iconsdir}/hicolor/*/apps/*
%{_iconsdir}/%name.png
%{_liconsdir}/%name.png
%{_miconsdir}/%name.png
%{_mandir}/man1/*
