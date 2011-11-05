# revision 23089
# category TLCore
# catalog-ctan /dviware/dvipdfm
# catalog-date 2011-01-01 13:56:40 +0100
# catalog-license lppl
# catalog-version 0.13.2d
Name:		texlive-dvipdfm
Version:	0.13.2d
Release:	1
Summary:	A DVI driver to produce PDF directly
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/dviware/dvipdfm
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvipdfm.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvipdfm.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvipdfm.x86_64-linux.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-dvipdfm.bin = %{EVRD}
Provides:	tetex-dvipdfm
Provides:	texlive-texmf-dvipdfm = 20111101
Obsoletes:	texlive-texmf-dvipdfm <= 2007
Conflicts:	texlive-texmf-dvipdfm <= 2007
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The driver offers a wide range of \special commands (including
a colour stack), and supports compression of data streams, etc.
Note that the extended version dvipdfmx will operate "as
dvipdfm" if necessary.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/dvipdft
%{_texmfdir}/dvipdfm/config/config
%{_texmfdir}/dvipdfm/config/config-win32
%{_texmfdir}/tex/latex/dvipdfm/dvipdfm.def
%doc %{_texmfdir}/doc/dvipdfm/Makefile
%doc %{_texmfdir}/doc/dvipdfm/dvipdfm.pdf
%doc %{_texmfdir}/doc/dvipdfm/dvipdfm.tex
%doc %{_texmfdir}/doc/dvipdfm/mwicks.bb
%doc %{_texmfdir}/doc/dvipdfm/mwicks.jpeg
%doc %{_texmfdir}/doc/dvipdfm/sample.tex
%doc %{_texmfdir}/doc/dvipdfm/something.bb
%doc %{_texmfdir}/doc/dvipdfm/something.eps
%doc %{_texmfdir}/doc/dvipdfm/something.fig
%doc %{_texmfdir}/doc/dvipdfm/something.pdf
%doc %{_texmfdir}/doc/dvipdfm/transistor.bb
%doc %{_texmfdir}/doc/dvipdfm/transistor.eps
%doc %{_texmfdir}/doc/dvipdfm/transistor.fig
%doc %{_texmfdir}/doc/dvipdfm/transistor.pdf
%doc %{_mandir}/man1/dvipdfm.1*
%doc %{_texmfdir}/doc/man/man1/dvipdfm.man1.pdf
%doc %{_mandir}/man1/dvipdft.1*
%doc %{_texmfdir}/doc/man/man1/dvipdft.man1.pdf
%doc %{_mandir}/man1/ebb.1*
%doc %{_texmfdir}/doc/man/man1/ebb.man1.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
# shell script
mkdir -p %{buildroot}%{_bindir}
cp -far bin/x86_64-linux/dvipdft %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
