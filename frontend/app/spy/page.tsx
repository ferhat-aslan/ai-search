import {AppSidebar} from "@/components/app-sidebar";
import {ChartAreaInteractive} from "@/components/chart-area-interactive";
import {DataTable} from "@/components/data-table";
import {SectionCards} from "@/components/section-cards";
import {SiteHeader} from "@/components/site-header";
import {SidebarInset, SidebarProvider} from "@/components/ui/sidebar";

import {keywords as data} from "@/app/data";
import {Input} from "@/components/ui/input";

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
            <div className="flex flex-col gap-4 py-4 md:gap-6 md:py-6 rounded-2xl bg-white shadow-lg w-full border border-gray-200 p-4 md:p-6">
              <span>Firecrawler, Openai Agents Web Search Preview</span>
              <Input className="w-full" placeholder="Search..." />
            </div>
          </div>
        </div>
      </SidebarInset>
    </SidebarProvider>
  );
}
