Summary:	LV2 MIDI extension - a data type for raw MIDI
Summary(pl.UTF-8):	Rozszerzenie LV2 MIDI - typ danych dla surowego MIDI
Name:		lv2-midi
Version:	1.4
Release:	1
License:	ISC
Group:		Libraries
Source0:	http://lv2plug.in/spec/%{name}-%{version}.tar.bz2
# Source0-md5:	de24efd1ef36e4db681ca7d0e939e82e
URL:		http://lv2plug.in/ns/ext/midi/
BuildRequires:	python >= 1:2.6
BuildRequires:	python-modules >= 1:2.6
Requires:	lv2core >= 6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LV2 MIDI extension defines a data type for a MIDI message,
midi:MidiEvent, which is normalized for fast and convenient processing
by plugins.

%description -l pl.UTF-8
Rozszerzenie LV2 MIDI definiuje typ danych dla komunikatów MIDI,
midi:MidiEvent - znormalizowany do szybkiego i wygodnego przetwarzania
przez wtyczki.

%package devel
Summary:	Development files for LV2 MIDI extension
Summary(pl.UTF-8):	Pliki programistyczne rozszerzenia LV2 MIDI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	lv2core-devel >= 6.0

%description devel
Development files for LV2 MIDI extension.

%description devel -l pl.UTF-8
Pliki programistyczne rozszerzenia LV2 MIDI.

%prep
%setup -q

%build
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}

./waf

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS
%dir %{_libdir}/lv2/midi.lv2
%{_libdir}/lv2/midi.lv2/midi.ttl
%{_libdir}/lv2/midi.lv2/manifest.ttl

%files devel
%defattr(644,root,root,755)
#%{_libdir}/lv2/midi.lv2/midi.h
%{_includedir}/lv2/lv2plug.in/ns/ext/midi
%{_pkgconfigdir}/lv2-lv2plug.in-ns-ext-midi.pc
