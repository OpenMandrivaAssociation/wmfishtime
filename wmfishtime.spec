%define version 1.24
%define release %mkrel 1
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

install -m 755 -d $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="%{_bindir}/%{name} -b" icon="%{name}.png"\\
                 needs="X11" section="Applications/Monitoring" title="WmFishTime"\\
                 longtitle="Analog clock in a tank fish"
EOF


%clean
[ -z $RPM_BUILD_ROOT ] || {
    rm -rf $RPM_BUILD_ROOT
}


%post
%{update_menus}


%postun
%{clean_menus}


%files
%defattr (-,root,root)
%doc ALL_I_GET_IS_A_GRAY_BOX CODING INSTALL README AUTHORS COPYING
%{_bindir}/*
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_menudir}/%{name}
%attr(644,root,man) %{_mandir}/man1/*

