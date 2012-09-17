%define gitdate 20120917

%define glumajor 1
%define gluname glu
%define libgluname %mklibname %{gluname} %{glumajor}
%define develglu %mklibname %{gluname} -d

%define rel	1

Name:		mesa-libGLU
Version:	9.0
Release:	%mkrel 0.git%{gitdate}.%{rel}
Summary:	Mesa libGLU library
Group:		System/Libraries
License:	MIT
URL:		http://mesa3d.org/
# snapshot only at this point
Source0:	libGLU-%{gitdate}.tar.xz
Source2:	make-git-snapshot.sh

%if 0%{?gitdate}
BuildRequires:	autoconf automake libtool
%endif
BuildRequires:	pkgconfig(gl)

%description
Mesa implementation of the standard GLU OpenGL utility API.

%package -n	%{libgluname}
Summary:	Files for Mesa (GLU libs)
Group:		System/Libraries
Provides:	libmesa%{gluname} = %{version}-%{release}
Obsoletes:	%{_lib}mesaglu1 < 8.0

%description -n %{libgluname}
GLU is the OpenGL Utility Library.
It provides a number of functions upon the base OpenGL library to provide
higher-level drawing routines from the more primitive routines provided by
OpenGL.

%package -n	%{develglu}
Summary:	Development files for GLU libs
Group:		Development/C
Requires:	%{libgluname} = %{version}-%{release}
Provides:	libmesa%{gluname}-devel = %{version}-%{release}
Provides:	mesa%{gluname}-devel = %{version}-%{release}
Obsoletes:	%{_lib}mesaglu1-devel < 8.0

%description -n %{develglu}
This package contains the headers needed to compile programs with GLU.

%prep
%setup -q -n libGLU-%{?gitdate:%{gitdate}}%{?!gitdate:%{version}}

%build
%if 0%{?gitdate}
autoreconf -v -i -f
%endif
%configure --disable-static
%make

%install
%makeinstall_std
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -rf %{buildroot}%{_datadir}/man/man3/gl[A-Z]*

%files -n %{libgluname}
%{_libdir}/libGLU.so.%{glumajor}*

%files -n %{develglu}
%{_includedir}/GL/glu.h
%{_includedir}/GL/glu_mangle.h
%{_libdir}/libGLU.so
%{_libdir}/pkgconfig/glu.pc
