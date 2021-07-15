def options(opt):
    opt.load('compiler_cxx')

def configure(cfg):
    cfg.check_waf_version(mini='1.7.5')
    cfg.load('compiler_cxx')

def build(bld):
    bld(name='revision', rule='sleep 10; echo "#define REVISION \\"`git rev-parse HEAD`\\"" > ${TGT}',
        target=bld.path.find_or_declare('revision.hpp'),
        always=True)
    bld(features='cxx', source='empty.cpp', name='empty', deps=['revision'])
    bld(features='cxx cxxprogram', source='test.cpp', name='test', target='test', deps=['empty'])
