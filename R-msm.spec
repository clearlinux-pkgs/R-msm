#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-msm
Version  : 1.6.6
Release  : 1
URL      : https://cran.r-project.org/src/contrib/msm_1.6.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/msm_1.6.6.tar.gz
Summary  : Multi-State Markov and Hidden Markov Models in Continuous Time
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-msm-lib
Requires: R-doParallel
Requires: R-expm
Requires: R-flexsurv
Requires: R-mvtnorm
BuildRequires : R-doParallel
BuildRequires : R-expm
BuildRequires : R-flexsurv
BuildRequires : R-mvtnorm
BuildRequires : clr-R-helpers

%description
Markov multi-state models to longitudinal data.  Designed for
    processes observed at arbitrary times in continuous time (panel data)
    but some other observation schemes are supported. Both Markov
    transition rates and the hidden Markov output process can be modelled
    in terms of covariates, which may be constant or piecewise-constant
    in time.

%package lib
Summary: lib components for the R-msm package.
Group: Libraries

%description lib
lib components for the R-msm package.


%prep
%setup -q -c -n msm

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530404513

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530404513
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library msm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library msm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library msm
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library msm|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/msm/CITATION
/usr/lib64/R/library/msm/DESCRIPTION
/usr/lib64/R/library/msm/INDEX
/usr/lib64/R/library/msm/Meta/Rd.rds
/usr/lib64/R/library/msm/Meta/data.rds
/usr/lib64/R/library/msm/Meta/features.rds
/usr/lib64/R/library/msm/Meta/hsearch.rds
/usr/lib64/R/library/msm/Meta/links.rds
/usr/lib64/R/library/msm/Meta/nsInfo.rds
/usr/lib64/R/library/msm/Meta/package.rds
/usr/lib64/R/library/msm/Meta/vignette.rds
/usr/lib64/R/library/msm/NAMESPACE
/usr/lib64/R/library/msm/NEWS
/usr/lib64/R/library/msm/R/msm
/usr/lib64/R/library/msm/R/msm.rdb
/usr/lib64/R/library/msm/R/msm.rdx
/usr/lib64/R/library/msm/data/Rdata.rdb
/usr/lib64/R/library/msm/data/Rdata.rds
/usr/lib64/R/library/msm/data/Rdata.rdx
/usr/lib64/R/library/msm/doc/index.html
/usr/lib64/R/library/msm/doc/msm-manual.R
/usr/lib64/R/library/msm/doc/msm-manual.pdf
/usr/lib64/R/library/msm/help/AnIndex
/usr/lib64/R/library/msm/help/aliases.rds
/usr/lib64/R/library/msm/help/msm.rdb
/usr/lib64/R/library/msm/help/msm.rdx
/usr/lib64/R/library/msm/help/paths.rds
/usr/lib64/R/library/msm/html/00Index.html
/usr/lib64/R/library/msm/html/R.css
/usr/lib64/R/library/msm/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/msm/libs/msm.so
/usr/lib64/R/library/msm/libs/msm.so.avx2
/usr/lib64/R/library/msm/libs/msm.so.avx512
