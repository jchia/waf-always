def options(opt):
    opt.load('compiler_cxx')

def configure(cfg):
    cfg.check_waf_version(mini='2.0.20')
    cfg.load('compiler_cxx')
    cfg.env.prepend_value('INCLUDES', cfg.path.abspath() + '/codegen_include')
    cfg.env.prepend_value('INCLUDES', cfg.path.abspath() + '/include')

def build(bld):
    bld.recurse('app lib')
