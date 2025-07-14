# NOTE: g++ eats 700+MB of memory
#
# Conditional build:
%bcond_with	openmp		# OpenMP support (incompatible with image-cache)
%bcond_without	tcmalloc	# use of Google TCMalloc library
#
Summary:	Image blending with multiresolution splines
Summary(pl.UTF-8):	Łączenie zdjęć przy użyciu splajnów wielokrotnej rozdzielczości
Name:		enblend-enfuse
Version:	4.2
Release:	5
License:	GPL v2+
Group:		Applications/Graphics
Source0:	https://downloads.sourceforge.net/enblend/%{name}-%{version}.tar.gz
# Source0-md5:	e26751f393862cecfd1a113003787001
Patch0:		gcc11.patch
URL:		https://enblend.sourceforge.net/
BuildRequires:	OpenEXR-devel >= 1.0
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	boost-devel >= 1.55
%{?with_openmp:BuildRequires:	gcc-c++ >= 6:4.2}
BuildRequires:	glew-devel
BuildRequires:	gnuplot
BuildRequires:	gsl-devel
BuildRequires:	help2man
BuildRequires:	lcms2-devel >= 2
%{?with_openmp:BuildRequires:	libgomp-devel}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel >= 5:4.3
%{?with_tcmalloc:BuildRequires:	libtcmalloc-devel}
BuildRequires:	libtiff-devel
BuildRequires:	perl-TimeDate
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	texinfo
BuildRequires:	tidy
BuildRequires:	transfig
BuildRequires:	vigra-devel >= 1.8
BuildRequires:	zlib-devel
Requires:	vigra >= 1.8
Provides:	enblend = %{version}
Obsoletes:	enblend
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enblend is a tool for compositing images. Given a set of images that
overlap in some irregular way, Enblend overlays them in such a way
that the seam between the images is invisible, or at least very
difficult to see. Enblend does not line up the images for you. Use a
tool like Hugin to do that.

%description -l pl.UTF-8
Enblend to narzędzie do łączenia zdjęć. Po przekazaniu zbioru zdjęć
nachodzących na siebie w jakiś nieregularny sposób Enblend nakłada je
w taki sposób, że połączenia między zdjęciami są niewidoczne, albo
przynajmniej bardzo trudne do zobaczenia. Enblend nie wyrównuje zdjęć
- do tego można użyć narzędzia takiego jak Hugin.

%prep
%setup -q
%patch -P0 -p1

%build
export CXXFLAGS="%{rpmcxxflags} -std=gnu++14"
%configure \
	%{?with_openmp:--enable-openmp --disable-image-cache}
	%{!?with_tcmalloc:--without-tcmalloc}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/enblend
%attr(755,root,root) %{_bindir}/enfuse
%{_mandir}/man1/enblend.1*
%{_mandir}/man1/enfuse.1*
