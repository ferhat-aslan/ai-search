import {AppSidebar} from "@/components/app-sidebar";
import {ChartAreaInteractive} from "@/components/chart-area-interactive";
import {DataTable} from "@/components/data-table";
import {SectionCards} from "@/components/section-cards";
import {SiteHeader} from "@/components/site-header";
import {SidebarInset, SidebarProvider} from "@/components/ui/sidebar";

import {keywords as data} from "@/app/data";

export default function Page() {
  return (
    <SidebarProvider
      style={
        {
          "--sidebar-width": "calc(var(--spacing) * 72)",
          "--header-height": "calc(var(--spacing) * 12)",
        } as React.CSSProperties
      }
    >
      <AppSidebar variant="inset" />
      <SidebarInset>
        <SiteHeader />
        <div className="flex flex-1 flex-col">
          <div className="@container/main flex flex-1 flex-col gap-2 justify-center items-center">
            <ul className="flex flex-col gap-2 p-4 md:p-6 rounded-md shadow bg-white w-full max-w-2xl">
              <li className="text-sm text-gray-600">
                📄 Structured Data (Schema Markup)
              </li>
              <li className="text-sm text-gray-600">
                🛒 Microsoft Merchant Center
              </li>
              <li className="text-sm text-gray-600">🌐 Bing Webmaster Tools</li>
              <li className="text-sm text-gray-600">
                🤖 robots.txt Configuration (Allow AI Crawling)
              </li>
              <li className="text-sm text-gray-600">
                🔗 Internal Linking Strategy
              </li>
              <li className="text-sm text-gray-600">
                📈 Performance Monitoring (Google Analytics, Search Console)
              </li>
              <li className="text-sm text-gray-600">
                🔍 Keyword Research and Optimization
              </li>
              <li className="text-sm text-gray-600">📱 Mobile Optimization</li>
            </ul>
          </div>
        </div>
      </SidebarInset>
    </SidebarProvider>
  );
}
