#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-plm
Version  : 1.6.6
Release  : 2
URL      : https://cran.r-project.org/src/contrib/plm_1.6-6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/plm_1.6-6.tar.gz
Summary  : Linear Models for Panel Data
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-Formula
Requires: R-bdsmatrix
Requires: R-lmtest
Requires: R-maxLik
Requires: R-pbkrtest
BuildRequires : R-Formula
BuildRequires : R-bdsmatrix
BuildRequires : R-lmtest
BuildRequires : R-maxLik
BuildRequires : R-pbkrtest
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n plm

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521214347

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521214347
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library plm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library plm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library plm
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library plm|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/plm/CITATION
/usr/lib64/R/library/plm/DESCRIPTION
/usr/lib64/R/library/plm/INDEX
/usr/lib64/R/library/plm/Meta/Rd.rds
/usr/lib64/R/library/plm/Meta/data.rds
/usr/lib64/R/library/plm/Meta/features.rds
/usr/lib64/R/library/plm/Meta/hsearch.rds
/usr/lib64/R/library/plm/Meta/links.rds
/usr/lib64/R/library/plm/Meta/nsInfo.rds
/usr/lib64/R/library/plm/Meta/package.rds
/usr/lib64/R/library/plm/Meta/vignette.rds
/usr/lib64/R/library/plm/NAMESPACE
/usr/lib64/R/library/plm/NEWS
/usr/lib64/R/library/plm/R/plm
/usr/lib64/R/library/plm/R/plm.rdb
/usr/lib64/R/library/plm/R/plm.rdx
/usr/lib64/R/library/plm/data/Cigar.rda
/usr/lib64/R/library/plm/data/Crime.rda
/usr/lib64/R/library/plm/data/EmplUK.rda
/usr/lib64/R/library/plm/data/Gasoline.rda
/usr/lib64/R/library/plm/data/Grunfeld.rda
/usr/lib64/R/library/plm/data/Hedonic.rda
/usr/lib64/R/library/plm/data/LaborSupply.rda
/usr/lib64/R/library/plm/data/Males.rda
/usr/lib64/R/library/plm/data/Parity.rda
/usr/lib64/R/library/plm/data/Produc.rda
/usr/lib64/R/library/plm/data/RiceFarms.rda
/usr/lib64/R/library/plm/data/Snmesp.rda
/usr/lib64/R/library/plm/data/SumHes.rda
/usr/lib64/R/library/plm/data/Wages.rda
/usr/lib64/R/library/plm/doc/index.html
/usr/lib64/R/library/plm/doc/plm.R
/usr/lib64/R/library/plm/doc/plm.pdf
/usr/lib64/R/library/plm/doc/plm.rnw
/usr/lib64/R/library/plm/help/AnIndex
/usr/lib64/R/library/plm/help/aliases.rds
/usr/lib64/R/library/plm/help/paths.rds
/usr/lib64/R/library/plm/help/plm.rdb
/usr/lib64/R/library/plm/help/plm.rdx
/usr/lib64/R/library/plm/html/00Index.html
/usr/lib64/R/library/plm/html/R.css
