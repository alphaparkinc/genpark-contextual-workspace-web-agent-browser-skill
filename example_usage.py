from client import ContextualWorkspaceWebAgentBrowserClient

def main():
    client = ContextualWorkspaceWebAgentBrowserClient()
    res = client.orchestrate_browser_spaces_and_boosts('RESEARCH_AND_PAPERS', 'Synthesize arXiv paper PDF annotations')
    print('Space ID: ' + res['browser_space_id'] + ' | ' + res['space_name'])
    print('Pinned Tabs: ' + str(res['pinned_tabs_isolated_count']) + ' | Memory Saved: ' + str(res['tab_memory_reduction_pct']) + '%')
    print('AI Sidebar Ready: ' + str(res['contextual_ai_sidebar_page_synthesized']) + ' (Auto-Archived: ' + str(res['clutter_auto_archive_tabs_purged']) + ')')

if __name__ == '__main__':
    main()
