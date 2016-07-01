################################  NOTE  ########################################
# If you add a new feature flag - CREATE A TASK TO REMOVE IT as soon as
# new functionality proved it works properly on prod server. We have to keep
# our code clean without mess of legacy feature flags
################################################################################
# Docs url  -  https://gargoyle-yplan.readthedocs.io/en/latest/install.html

FRONTEND_TITLE_FEATURE = 'frontend_title_feature'
NAZI_FEATURE = 'nazi_feature'

GARGOYLE_SWITCH_DEFAULTS = {
    FRONTEND_TITLE_FEATURE: {
        'is_active': False,
        'label': 'Frontend title feature',
        'description': 'Show different title on landing page',
    },
    NAZI_FEATURE: {
        'is_active': False,
        'label': 'Nazi theme feature',
        'description': 'Show fancy background landing page',
    },
}
