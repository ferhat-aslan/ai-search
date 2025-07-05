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
            <div className="flex flex-col gap-4 py-4 md:gap-6 md:py-6 justify-center items-center">
              <div className=" grid grid-cols-2 grid-template-rows-2 gap-4">
                <span className="bg-sidebar rounded-2xl p-4 flex flex-col justify-start items-start gap-2 ">
                  <span className="flex flex-row justify-start items-center gap-2">
                    <h1 className="text-lg font-semibold">site:Tiktok</h1>
                  </span>
                  <span>Most Popular Competitor: Tesla</span>
                  <span>Most Popular Keywords: American EV Car Startup</span>
                </span>
                <span className="bg-sidebar rounded-2xl p-4 flex flex-col justify-start items-start gap-2 ">
                  <span className="flex flex-row justify-start items-center gap-2">
                    <h1 className="text-lg font-semibold">site:Facebook</h1>
                  </span>
                  <span>Most Popular Competitor: Rivian</span>
                  <span>Most Popular Keywords: American EV Car Startup</span>
                </span>
                <span className="bg-sidebar rounded-2xl p-4 flex flex-col justify-start items-start gap-2 ">
                  <span className="flex flex-row justify-start items-center gap-2">
                    <h1 className="text-lg font-semibold">site:Twitter/X</h1>
                  </span>
                  <span>Most Popular Competitor: Rivian</span>
                  <span>Most Popular Keywords: American EV Car Startup</span>
                </span>
                <span className="bg-sidebar rounded-2xl p-4 flex flex-col justify-start items-start gap-2 ">
                  <span className="flex flex-row justify-start items-center gap-2">
                    <h1 className="text-lg font-semibold">site:Youtube</h1>
                  </span>
                  <span>Most Popular Competitor: Rivian</span>
                  <span>Most Popular Keywords: American EV Car Startup</span>
                </span>
              </div>
            </div>
          </div>
        </div>
      </SidebarInset>
    </SidebarProvider>
  );
}
