# NOTE: g++ eats 700+MB of memory
#
# Conditional build:
%bcond_with	gomp	# OpenMP support (incompatible with image-cache)
#
Summary:	Image blending with multiresolution splines
Summary(pl.UTF-8):	Łączenie zdjęć przy użyciu splajnów wielokrotnej rozdzielczości
Name:		enblend-enfuse
Version:	4.1.2
Release:	9
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/enblend/%{name}-%{version}.tar.gz
# Source0-md5:	5b609ddfc9fae5fadf65d29c08e0340e
Patch0:		%{name}-info.patch
Patch1:		%{name}-texinfo.patch
URL:		http://enblend.sourceforge.net/
BuildRequires:	OpenEXR-devel >= 1.0
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	boost-devel >= 1.35.0
%{?with_gomp:BuildRequires:	gcc-c++ >= 6:4.2}
BuildRequires:	glew-devel
BuildRequires:	gsl-devel
BuildRequires:	help2man
BuildRequires:	gnuplot
BuildRequires:	lcms2-devel >= 2
%{?with_gomp:BuildRequires:	libgomp-devel}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel >= 5:3.4
BuildRequires:	libtiff-devel
BuildRequires:	libxmi-devel
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
%patch0 -p1
%patch1 -p1

%{__sed} -i -e 's/src:://g;s/CFG::/CFG_/g' doc/*.texi doc/define2set.pl configure.in

%build
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	%{?with_gomp:--enable-openmp --disable-image-cache}
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
%{_infodir}/enblend.info*
%{_infodir}/enfuse.info*
