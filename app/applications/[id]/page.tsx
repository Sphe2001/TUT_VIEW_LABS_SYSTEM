'use client';

import { application } from "../../../components/common/Application";
import React, { useState, useEffect } from 'react';
import  AppsList  from "@/components/common/AppsList";



export default function Page() {
	const [applications, setApplication] = useState<application[]>([]);

    useEffect(() => {
			const fetchData = async () => {
				try {
					const res = await fetch("http://localhost:8000/api/applications");
					if (!res.ok) {
						throw new Error('Failed to fetch applications');
					}
					const data: application[] = await res.json();
					setApplication(data);
				} catch (error) {
					console.error(error);
				}
			};

			fetchData();
		}, []);

  

	return(
        <div >
			<header className='bg-white shadow'>
				<div className='mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8'>
					<h1 className='text-3xl font-bold tracking-tight text-gray-900'>
						Applications
					</h1>
				</div>
                <section className="" >
                    {applications.map(app => (
                        <AppsList key={app.id} props={app} />
                    ))}
			    </section>
			</header>
        </div>
    );
	
}
