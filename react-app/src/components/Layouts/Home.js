import React from 'react'

export default function Home(){
    return (
        <div>
            <h1>THIS IS THE HOME PAGE</h1>
            <div id="accordianId" role="tablist" aria-multiselectable="true">
                <div class="card">
                    <div class="card-header" role="tab" id="section1HeaderId">
                        <h5 class="mb-0">
                            <a data-toggle="collapse" data-parent="#accordianId" href="#section1ContentId" aria-expanded="true" aria-controls="section1ContentId">
                      Section 1
                    </a>
                        </h5>
                    </div>
                    <div id="section1ContentId" class="collapse in" role="tabpanel" aria-labelledby="section1HeaderId">
                        <div class="card-body">
                            Section 1 content
                        </div>
                    </div>
                </div>
                <div class="card">
                    <div class="card-header" role="tab" id="section2HeaderId">
                        <h5 class="mb-0">
                            <a data-toggle="collapse" data-parent="#accordianId" href="#section2ContentId" aria-expanded="true" aria-controls="section2ContentId">
                      Section 2
                    </a>
                        </h5>
                    </div>
                    <div id="section2ContentId" class="collapse in" role="tabpanel" aria-labelledby="section2HeaderId">
                        <div class="card-body">
                            Section 2 content
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

