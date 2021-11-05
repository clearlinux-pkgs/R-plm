#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-plm
Version  : 2.4.3
Release  : 53
URL      : https://cran.r-project.org/src/contrib/plm_2.4-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/plm_2.4-3.tar.gz
Summary  : Linear Models for Panel Data
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-Formula
Requires: R-Rdpack
Requires: R-bdsmatrix
Requires: R-lmtest
Requires: R-maxLik
Requires: R-sandwich
Requires: R-zoo
BuildRequires : R-Formula
BuildRequires : R-Rdpack
BuildRequires : R-bdsmatrix
BuildRequires : R-lmtest
BuildRequires : R-maxLik
BuildRequires : R-sandwich
BuildRequires : R-zoo
BuildRequires : buildreq-R

%description
# The `plm` Package - Linear Models and Tests for Panel Data
<!-- badges: start -->
[![CRAN status](https://www.r-pkg.org/badges/version/plm)](https://CRAN.R-project.org/package=plm)
[![CRAN check](https://cranchecks.info/badges/summary/plm)](https://cran.r-project.org/web/checks/check_results_plm.html)
[![Downloads](https://cranlogs.r-pkg.org/badges/plm)](https://CRAN.R-project.org/package=plm)
<!-- badges: end -->

%prep
%setup -q -c -n plm
cd %{_builddir}/plm

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633446518

%install
export SOURCE_DATE_EPOCH=1633446518
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize " >> ~/.R/Makevars
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
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc plm || :


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
/usr/lib64/R/library/plm/NEWS.md
/usr/lib64/R/library/plm/R/plm
/usr/lib64/R/library/plm/R/plm.rdb
/usr/lib64/R/library/plm/R/plm.rdx
/usr/lib64/R/library/plm/REFERENCES.bib
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
/usr/lib64/R/library/plm/doc/A_plmPackage.R
/usr/lib64/R/library/plm/doc/A_plmPackage.Rmd
/usr/lib64/R/library/plm/doc/A_plmPackage.html
/usr/lib64/R/library/plm/doc/B_plmFunction.R
/usr/lib64/R/library/plm/doc/B_plmFunction.Rmd
/usr/lib64/R/library/plm/doc/B_plmFunction.html
/usr/lib64/R/library/plm/doc/C_plmModelComponents.R
/usr/lib64/R/library/plm/doc/C_plmModelComponents.Rmd
/usr/lib64/R/library/plm/doc/C_plmModelComponents.html
/usr/lib64/R/library/plm/doc/index.html
/usr/lib64/R/library/plm/help/AnIndex
/usr/lib64/R/library/plm/help/aliases.rds
/usr/lib64/R/library/plm/help/paths.rds
/usr/lib64/R/library/plm/help/plm.rdb
/usr/lib64/R/library/plm/help/plm.rdx
/usr/lib64/R/library/plm/html/00Index.html
/usr/lib64/R/library/plm/html/R.css
/usr/lib64/R/library/plm/removed/dynformula.Rd
/usr/lib64/R/library/plm/removed/pFormula.Rd
/usr/lib64/R/library/plm/removed/plm.data.Rd
/usr/lib64/R/library/plm/removed/test_model.matrix_pmodel.response_NA.R
/usr/lib64/R/library/plm/removed/unused.R
/usr/lib64/R/library/plm/tests/test_Chow.R
/usr/lib64/R/library/plm/tests/test_Chow.Rout.save
/usr/lib64/R/library/plm/tests/test_Errors.R
/usr/lib64/R/library/plm/tests/test_Errors.Rout.save
/usr/lib64/R/library/plm/tests/test_Estimators.R
/usr/lib64/R/library/plm/tests/test_Estimators.Rout.save
/usr/lib64/R/library/plm/tests/test_EstimatorsIV.R
/usr/lib64/R/library/plm/tests/test_EstimatorsIV.Rout.save
/usr/lib64/R/library/plm/tests/test_EstimatorsNested.R
/usr/lib64/R/library/plm/tests/test_EstimatorsNested.Rout.save
/usr/lib64/R/library/plm/tests/test_Evaluation.R
/usr/lib64/R/library/plm/tests/test_FD_models.R
/usr/lib64/R/library/plm/tests/test_FD_models.Rout.save
/usr/lib64/R/library/plm/tests/test_R2_adj_R2.R
/usr/lib64/R/library/plm/tests/test_as.data.frame_as.matrix.R
/usr/lib64/R/library/plm/tests/test_as.list.pdata.frame.R
/usr/lib64/R/library/plm/tests/test_cipstest.R
/usr/lib64/R/library/plm/tests/test_cipstest.Rout.save
/usr/lib64/R/library/plm/tests/test_clubSandwich_interoperability.R
/usr/lib64/R/library/plm/tests/test_detect_lin_dep_alias.R
/usr/lib64/R/library/plm/tests/test_fitted.plm.R
/usr/lib64/R/library/plm/tests/test_fixef.R
/usr/lib64/R/library/plm/tests/test_fixef.Rout.save
/usr/lib64/R/library/plm/tests/test_fixef2.R
/usr/lib64/R/library/plm/tests/test_fixef2.Rout.save
/usr/lib64/R/library/plm/tests/test_fixef_comp_lm_plm.R
/usr/lib64/R/library/plm/tests/test_fixef_comp_lm_plm.Rout.save
/usr/lib64/R/library/plm/tests/test_groupGenerics_pseries.R
/usr/lib64/R/library/plm/tests/test_groupGenerics_pseries.Rout.save
/usr/lib64/R/library/plm/tests/test_is.pconsecutive.R
/usr/lib64/R/library/plm/tests/test_is.pconsecutive.Rout.save
/usr/lib64/R/library/plm/tests/test_lag_lead.R
/usr/lib64/R/library/plm/tests/test_lag_lead.Rout.save
/usr/lib64/R/library/plm/tests/test_lagt_leadt.R
/usr/lib64/R/library/plm/tests/test_lagt_leadt.Rout.save
/usr/lib64/R/library/plm/tests/test_make.pconsecutive_pbalanced.R
/usr/lib64/R/library/plm/tests/test_make.pconsecutive_pbalanced.Rout.save
/usr/lib64/R/library/plm/tests/test_misc.R
/usr/lib64/R/library/plm/tests/test_misc.Rout.save
/usr/lib64/R/library/plm/tests/test_model.frame.R
/usr/lib64/R/library/plm/tests/test_model.frame.Rout.save
/usr/lib64/R/library/plm/tests/test_model.matrix_effects.R
/usr/lib64/R/library/plm/tests/test_model.matrix_effects.Rout.save
/usr/lib64/R/library/plm/tests/test_model.matrix_pmodel.response.R
/usr/lib64/R/library/plm/tests/test_model.matrix_pmodel.response.Rout.save
/usr/lib64/R/library/plm/tests/test_order_between_fixef_ranef.R
/usr/lib64/R/library/plm/tests/test_order_between_fixef_ranef.Rout.save
/usr/lib64/R/library/plm/tests/test_pFtest.R
/usr/lib64/R/library/plm/tests/test_pFtest.Rout.save
/usr/lib64/R/library/plm/tests/test_pbgtest.R
/usr/lib64/R/library/plm/tests/test_pbnftest.R
/usr/lib64/R/library/plm/tests/test_pbnftest.Rout.save
/usr/lib64/R/library/plm/tests/test_pbsytest_unbalanced.R
/usr/lib64/R/library/plm/tests/test_pbsytest_unbalanced.Rout.save
/usr/lib64/R/library/plm/tests/test_pcdtest.R
/usr/lib64/R/library/plm/tests/test_pcdtest.Rout.save
/usr/lib64/R/library/plm/tests/test_pdata.frame_const_allNA_nonfinite.R
/usr/lib64/R/library/plm/tests/test_pdata.frame_extract_class_est_mod.R
/usr/lib64/R/library/plm/tests/test_pdata.frame_id_index_more.R
/usr/lib64/R/library/plm/tests/test_pdata.frame_id_index_more.Rout.save
/usr/lib64/R/library/plm/tests/test_pdata.frame_print_duplicated_rownames.R
/usr/lib64/R/library/plm/tests/test_pdata.frame_pseriesfy.R
/usr/lib64/R/library/plm/tests/test_pdata.frame_pseriesfy.Rout.save
/usr/lib64/R/library/plm/tests/test_pdata.frame_subsetting.R
/usr/lib64/R/library/plm/tests/test_pdata.frame_subsetting.Rout.save
/usr/lib64/R/library/plm/tests/test_pdata.frame_unused_levels.R
/usr/lib64/R/library/plm/tests/test_pdiff_fd.R
/usr/lib64/R/library/plm/tests/test_pdiff_fd.Rout.save
/usr/lib64/R/library/plm/tests/test_pdwtest.R
/usr/lib64/R/library/plm/tests/test_pdwtest.Rout.save
/usr/lib64/R/library/plm/tests/test_pggls.R
/usr/lib64/R/library/plm/tests/test_pgmm.R
/usr/lib64/R/library/plm/tests/test_pgmm.Rout.save
/usr/lib64/R/library/plm/tests/test_pgrangertest.R
/usr/lib64/R/library/plm/tests/test_pgrangertest.Rout.save
/usr/lib64/R/library/plm/tests/test_pht.R
/usr/lib64/R/library/plm/tests/test_pht.Rout.save
/usr/lib64/R/library/plm/tests/test_phtest_Hausman_regression.R
/usr/lib64/R/library/plm/tests/test_phtest_Hausman_regression.Rout.save
/usr/lib64/R/library/plm/tests/test_plm.data.R
/usr/lib64/R/library/plm/tests/test_plm_na.action.R
/usr/lib64/R/library/plm/tests/test_plmtest_unbalanced.R
/usr/lib64/R/library/plm/tests/test_plmtest_unbalanced.Rout.save
/usr/lib64/R/library/plm/tests/test_preserve_rownames.R
/usr/lib64/R/library/plm/tests/test_pseries_subsetting.R
/usr/lib64/R/library/plm/tests/test_punbalancedness.R
/usr/lib64/R/library/plm/tests/test_purtest.R
/usr/lib64/R/library/plm/tests/test_purtest.Rout.save
/usr/lib64/R/library/plm/tests/test_pvar.R
/usr/lib64/R/library/plm/tests/test_pvar.Rout.save
/usr/lib64/R/library/plm/tests/test_pvcm.R
/usr/lib64/R/library/plm/tests/test_pvcm.Rout.save
/usr/lib64/R/library/plm/tests/test_pwaldtest.R
/usr/lib64/R/library/plm/tests/test_pwaldtest.Rout.save
/usr/lib64/R/library/plm/tests/test_pwaldtest_vcovG_attr_cluster.R
/usr/lib64/R/library/plm/tests/test_pwaldtest_vcovG_attr_cluster.Rout.save
/usr/lib64/R/library/plm/tests/test_pwfdtest_pwartest.R
/usr/lib64/R/library/plm/tests/test_pwtest.R
/usr/lib64/R/library/plm/tests/test_ranef.R
/usr/lib64/R/library/plm/tests/test_ranef.Rout.save
/usr/lib64/R/library/plm/tests/test_residuals_overall_fitted_exp.R
/usr/lib64/R/library/plm/tests/test_summary.plm_vcov.R
/usr/lib64/R/library/plm/tests/test_summary.pseries_character_logical_factor.R
/usr/lib64/R/library/plm/tests/test_transformations.R
/usr/lib64/R/library/plm/tests/test_transformations_collapse.R
/usr/lib64/R/library/plm/tests/test_vcovG_lin_dep.R
/usr/lib64/R/library/plm/tests/test_within_intercept.R
/usr/lib64/R/library/plm/tests/test_within_intercept.Rout.save
