%define version 1.24
%define release %mkrel 5
%define name wmfishtime

Summary:	Analog clock with background fish tank in a dockapp
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Monitoring
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
URL:		http://www.ne.jp/asahi/linux/timecop/
BuildRequires:	gtk-devel
# Prefix:		/usr/X11R6
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Well, this is just your standard time dockapp. Top part has the clock face,
bottom part has day of the week, followed by day, followed by month. Yellow
hand counts seconds, green hand counts minutes, red hand counts hours. Few
seconds after startup there are at least 32 bubbles floating up behind the
clock face.  There are 4 fishes randomly swimming back and forth. If you move
your mouse inside the dockapp window, the fish will get scared and run away.
If you compiled in mail checking (default), then whenever you get new mail
in the file pointed to by the $MAIL variable, it will display green weed
partially blocking the day/month counter, to remind you to read your mail.
If $MAIL is not set, nothing happens.

%prep

%setup -q -n %{name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS `gtk-config --cflags` ${EXTRA}" \
%make
     
%install
[ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT

install -m 755 -d $RPM_BUILD_ROOT%{_miconsdir}
install -m 755 -d $RPM_BUILD_ROOT%{_iconsdir}
install -m 755 -d $RPM_BUILD_ROOT%{_liconsdir}
tar xOjf %SOURCE1 %{name}-16x16.png > $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
tar xOjf %SOURCE1 %{name}-32x32.png > $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
tar xOjf %SOURCE1 %{name}-48x48.png > $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_bindir}/
install -m 755 wmfishtime $RPM_BUILD_ROOT%{_bindir}/

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1/
bzip2 -9 -c wmfishtime.1 > $RPM_BUILD_ROOT%{_mandir}/man1/wmfishtime.1.bz2

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/%{name} -b
Icon=%{name}
Categories=System;Monitor;
Name=WmFishTime
Comment=Analog clock in a tank fish
EOF


%clean
[ -z $RPM_BUILD_ROOT ] || {
    rm -rf $RPM_BUILD_ROOT
}


%if %mdkversion < 200900
%post
%{update_menus}
%endif


%if %mdkversion < 200900
%postun
%{clean_menus}
%endif


%files
%defattr (-,root,root)
%doc ALL_I_GET_IS_A_GRAY_BOX CODING INSTALL README AUTHORS COPYING
%{_bindir}/*
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
%attr(644,root,man) %{_mandir}/man1/*



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.24-5mdv2010.0
+ Revision: 434855
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.24-4mdv2009.0
+ Revision: 262051
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.24-3mdv2009.0
+ Revision: 256140
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 20 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.24-1mdv2008.1
+ Revision: 135466
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- import wmfishtime


* Fri Jul 22 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.24-1mdk
- New release 1.24

* Thu Jun 02 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.23-5mdk
- Rebuild

* Tue Nov 25 2003 Marcel Pol <mpol@mandrake.org> 1.23-4mdk
- buildrequires
- remove redundant (build)requires

* Fri Jun 21 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.23-3mdk
- fix menu command entry (I am stupid)

* Fri Jun 21 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.23-2mdk
- png icons (out xpm!)
- s/Copyrigth/License/
- %%{_prefix} = /usr

* Fri Jun 08 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 1.23-1mdk
- Initial packaging.
